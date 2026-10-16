import copy
import csv
import json
import math
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from vpn_guard.capture import parse_tshark
from vpn_guard.common import load_config, new_output
from vpn_guard.demo import generate
from vpn_guard.features import Aggregator, FEATURES, Packet, extract
from vpn_guard.model import check_holdout, load_model, matrix, metrics, predict, save_model, train
from vpn_guard.performance import summarize
from vpn_guard.report import build_report
from vpn_guard.wireguard import collect_status, init_vpn, peer_events

CONFIG = load_config(Path(__file__).parents[1] / "config/lab.json")


class FeatureTests(unittest.TestCase):
    def packet(self, timestamp=1, src="10.77.0.2", dst="10.77.0.1", port=443, length=100, syn=0, rst=0):
        return Packet(timestamp, src, dst, 40000, port, length, syn, rst)

    def test_direction_statistics_and_window_boundary(self):
        packets = [self.packet(1, syn=1), self.packet(3, src="10.77.0.1", dst="10.77.0.2", port=40000, length=300, rst=1),
                   self.packet(10, port=80)]
        rows = extract(packets, CONFIG, "capture")
        first, second = rows
        self.assertEqual(first["packets"], 2)
        self.assertEqual(first["bytes"], 400)
        self.assertEqual(first["mean_packet_bytes"], 200)
        self.assertEqual(first["std_packet_bytes"], 100)
        self.assertEqual(first["mean_iat_ms"], 2000)
        self.assertEqual(first["syn_ratio"], 1)
        self.assertEqual(first["rst_ratio"], 0.5)
        self.assertEqual(first["outbound_ratio"], 0.5)
        self.assertEqual(first["unique_dst_ports"], 1)  # No ephemeral client ports counted.
        self.assertEqual(first["bytes_per_second"], 40)
        self.assertEqual(second["window_start"], 10)

    def test_scan_across_many_flows_and_ignored_outside_traffic(self):
        collector = Aggregator(CONFIG, "scan")
        for port in range(1, 25):
            collector.add(self.packet(port / 10, port=port, syn=1))
        collector.add(self.packet(3, src="192.0.2.4", dst="192.0.2.5"))
        self.assertEqual(collector.ignored_packets, 1)
        row = collector.flush()[0]
        self.assertEqual(row["unique_dst_ports"], 24)
        self.assertEqual(row["packets"], 24)

    def test_closed_windows_and_no_synthetic_idle_records(self):
        collector = Aggregator(CONFIG, "r")
        collector.add(self.packet())
        self.assertEqual(collector.flush(9), [])
        self.assertEqual(len(collector.flush(10)), 1)
        collector.add(self.packet(2))
        self.assertEqual(collector.late_packets, 1)
        self.assertEqual(collector.flush(50), [])

    def test_packet_validation(self):
        base = {"timestamp": "1", "src_ip": "10.77.0.2", "dst_ip": "10.77.0.1", "src_port": "1", "dst_port": "2",
                "length": "100", "syn": "0", "rst": "0", "protocol": "6"}
        for field, value in [("timestamp", "nan"), ("length", "-1"), ("src_ip", "bad"), ("dst_port", "65536"), ("syn", "2")]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                Packet.from_row({**base, field: value})

    def test_out_of_order_is_explicit(self):
        with self.assertRaisesRegex(ValueError, "orden temporal"):
            extract([self.packet(2), self.packet(1)], CONFIG, "r")

    def test_tshark_tcp_synack_udp_and_icmp(self):
        tcp = parse_tshark('"1.5","10.77.0.2","10.77.0.1","4000","443","","","60","1","0","0","6"')
        self.assertEqual(tcp.syn, 1)
        synack = parse_tshark('1.6,10.77.0.1,10.77.0.2,443,4000,,,60,1,1,0,6')
        self.assertEqual(synack.syn, 0)
        udp = parse_tshark('2,10.77.0.2,10.77.0.1,,,5000,53,100,,,,17')
        self.assertEqual(udp.dst_port, 53)
        icmp = parse_tshark('3,10.77.0.2,10.77.0.1,,,,,84,,,,1')
        self.assertEqual(icmp.dst_port, 0)


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.training, cls.testing = generate(CONFIG, Path(cls.tmp.name), seed=42)
        cls.artifact = train(cls.training)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_group_holdout_and_train_only_scaler(self):
        check_holdout(self.artifact, self.testing)
        self.assertEqual(self.artifact["pipeline"][0].n_samples_seen_, len(self.training))
        with self.assertRaisesRegex(ValueError, "Fuga de datos"):
            check_holdout(self.artifact, self.training[:3])

    def test_roundtrip_prediction(self):
        path = Path(self.tmp.name) / "model.joblib"
        save_model(self.artifact, path)
        loaded = load_model(path)
        a = predict(self.testing[:4], CONFIG, self.artifact)
        b = predict(self.testing[:4], CONFIG, loaded)
        self.assertEqual([r["probability"] for r in a], [r["probability"] for r in b])

    def test_model_ignores_identity_and_labels(self):
        sample = self.testing[:2]
        changed = [{**row, "peer_ip": "192.0.2.1", "label": "normal", "scenario": "changed", "run_id": "other"} for row in sample]
        a = predict(sample, CONFIG, self.artifact)
        b = predict(changed, CONFIG, self.artifact)
        self.assertEqual([r["probability"] for r in a], [r["probability"] for r in b])

    def test_invalid_training_and_window_mismatch(self):
        with self.assertRaises(ValueError):
            train([r for r in self.training if r["label"] == "normal"])
        with self.assertRaises(ValueError):
            predict([{**self.testing[0], "window_seconds": 30}], CONFIG, self.artifact)
        with self.assertRaises(ValueError):
            matrix([{**self.testing[0], FEATURES[0]: math.inf}])
        with self.assertRaisesRegex(ValueError, "duplicada"):
            predict([self.testing[0], self.testing[0]], CONFIG)

    def test_rules_work_without_model_and_high_volume_is_visible(self):
        row = {**self.testing[0], "unique_dst_ports": 30, "bytes_per_second": 2000000}
        prediction = predict([row], CONFIG)[0]
        self.assertEqual(prediction["alert"], 1)
        self.assertEqual(prediction["ml_alert"], 0)
        self.assertEqual(prediction["probability"], "")
        self.assertIn("volumen_elevado", prediction["reasons"])

    def test_confusion_matrix_and_undefined_metrics(self):
        rows = [{"label": label, "alert": alert} for label, alert in [
            ("normal", 0), ("normal", 1), ("anomaly", 0), ("anomaly", 1), ("anomaly", 1)]]
        m = metrics(rows)
        self.assertEqual(m["confusion_matrix"], {"TN": 1, "FP": 1, "FN": 1, "TP": 2})
        self.assertEqual(m["accuracy"], 0.6)
        self.assertAlmostEqual(m["f1"], 2 / 3)
        self.assertEqual(m["false_positive_rate"], 0.5)
        self.assertIsNone(metrics([{"label": "", "alert": 1}])["accuracy"])
        self.assertIsNone(metrics([{"label": "normal", "alert": 0}])["recall"])

    def test_report_exports_truth_and_escapes_untrusted_names(self):
        with tempfile.TemporaryDirectory() as directory:
            row = {**self.testing[0], "peer_name": "<script>alert(1)</script>", "label": "normal", "unique_dst_ports": 100}
            predictions = predict([row], CONFIG, self.artifact)
            report = build_report(predictions, directory, CONFIG, self.artifact)
            self.assertEqual(report["metrics_combined"]["confusion_matrix"]["FP"], 1)
            html = (Path(directory) / "reporte.html").read_text(encoding="utf-8")
            self.assertNotIn("<script>", html)
            self.assertIn("&lt;script&gt;", html)
            self.assertIn("simulados", html)
            with (Path(directory) / "errores.csv").open(encoding="utf-8", newline="") as stream:
                self.assertEqual(len(list(csv.DictReader(stream))), 1)

    def test_empty_capture_report_does_not_claim_accuracy(self):
        with tempfile.TemporaryDirectory() as directory:
            report = build_report([], directory, CONFIG)
            self.assertEqual(report["windows"], 0)
            self.assertIsNone(report["metrics_combined"]["accuracy"])
            self.assertIn("Sin ventanas completas", (Path(directory) / "reporte.html").read_text(encoding="utf-8"))


class WireGuardTests(unittest.TestCase):
    def test_status_uses_no_secret_dump(self):
        def execute(args, timeout=8):
            self.assertNotIn("dump", args)
            self.assertNotIn("showconf", args)
            return {"latest-handshakes": "PUB\t0\n", "transfer": "PUB\t100\t200\n",
                    "endpoints": "PUB\t192.0.2.1:10000\n", "allowed-ips": "PUB\t10.77.0.2/32\n"}.get(args[-1], "")
        with patch("vpn_guard.wireguard.command", side_effect=execute):
            result = collect_status(CONFIG)
        self.assertEqual(result["peers"][0]["state"], "never")
        self.assertEqual(result["peers"][0]["rx_bytes"], 100)

    def test_counter_resets_and_state_transitions(self):
        current = {"at": "now", "errors": [], "peers": [{"public_key": "pub", "rx_bytes": 20, "tx_bytes": 30,
                   "state": "stale", "allowed_ips": []}]}
        previous = copy.deepcopy(current)
        previous["peers"][0].update(state="recent", rx_bytes=100)
        events = peer_events(previous, current)
        self.assertEqual({e["event"] for e in events}, {"counter_reset", "handshake_state"})

    def test_missing_tools_diagnosed(self):
        with patch("vpn_guard.wireguard.command", side_effect=FileNotFoundError("wg")):
            status = collect_status(CONFIG)
        self.assertEqual(len(status["errors"]), 2)

    def test_reject_configuration_injection_and_output_overwrite(self):
        with self.assertRaises(ValueError):
            init_vpn("example.com:51820\nPostUp=bad", 2, "unused")
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory) / "evidence.txt").write_text("keep")
            with self.assertRaises(ValueError):
                new_output(directory)

    def test_generated_client_scope_and_private_keys_not_in_inventory(self):
        with tempfile.TemporaryDirectory() as directory:
            private = "A" * 43 + "="
            public = "B" * 43 + "="
            with patch("vpn_guard.wireguard.shutil.which", return_value="wg"), \
                    patch("vpn_guard.wireguard.command", return_value=private), \
                    patch("vpn_guard.wireguard.subprocess.run") as run:
                run.return_value.stdout = public
                init_vpn("192.0.2.10:51820", 2, directory)
            client = (Path(directory) / "cliente-1.conf").read_text()
            server = (Path(directory) / "wg0.conf").read_text()
            self.assertIn("AllowedIPs = 10.77.0.1/32", client)
            self.assertIn("AllowedIPs = 10.77.0.2/32", server)
            self.assertNotIn(private, (Path(directory) / "lab.json").read_text())
            self.assertEqual(server.count("[Peer]"), 2)


class CaptureLifecycleTests(unittest.TestCase):
    def capture(self, directory, returncode):
        from vpn_guard.capture import monitor
        # A fake tshark stream tests real capture orchestration without a network interface.
        class FakeProcess:
            def __init__(self):
                self.stdout = io.StringIO('21,10.77.0.2,10.77.0.1,4000,443,,,60,1,0,0,6\n')
                self.returncode = returncode
            def poll(self):
                return self.returncode
            def wait(self, timeout=None):
                return self.returncode
        # Construct Path before mocking os.name (pathlib chooses Windows/Posix from it).
        output = Path(directory)
        previous = {"at": "now", "peers": [], "errors": []}
        calls = [0]
        def clock():
            calls[0] += 1
            return 10.1 if calls[0] <= 2 else 31.1
        with patch("vpn_guard.capture.os.name", "posix"), \
                patch("vpn_guard.capture.shutil.which", return_value="tshark"), \
                patch("vpn_guard.capture.subprocess.Popen", return_value=FakeProcess()), \
                patch("vpn_guard.capture.collect_status", return_value=previous), \
                patch("vpn_guard.capture.time.time", side_effect=clock), \
                patch("vpn_guard.capture.write_json") as write, \
                patch("vpn_guard.capture.build_report") as report:
            if returncode:
                with self.assertRaisesRegex(ValueError, "Captura fallida"):
                    monitor(CONFIG, output, 30)
            else:
                result = monitor(CONFIG, output, 30)
                self.assertEqual(result["windows"], 1)
                self.assertEqual(result["state"], "finished")
            self.assertTrue(report.called)
            final_manifest = write.call_args.args[1]
            self.assertEqual(final_manifest["state"], "failed" if returncode else "finished")

    def test_success_preserves_features_and_capture_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            self.capture(directory, 0)
            with (Path(directory) / "ventanas.csv").open(newline="", encoding="utf-8") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(rows[0]["source"], "real")
            self.assertEqual(rows[0]["window_start"], "20")

    def test_failed_capture_reports_failure_instead_of_success(self):
        with tempfile.TemporaryDirectory() as directory:
            self.capture(directory, 2)


class PerformanceTests(unittest.TestCase):
    def test_iperf_metrics_and_missing_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capture = root / "normal.json"
            capture.write_text(json.dumps({"end": {"sum_received": {"bits_per_second": 5000000, "bytes": 10000, "seconds": 2},
                                                   "sum_sent": {"retransmits": 4}}}))
            result = summarize([capture], root)
            self.assertEqual(result["streams"]["normal"]["mean_mbps"], 5)
            self.assertIsNone(result["streams"]["normal"]["std_mbps"])
            capture.write_text('{"error": "connection refused"}')
            with self.assertRaisesRegex(ValueError, "falló"):
                summarize([capture], root)


if __name__ == "__main__":
    unittest.main()
