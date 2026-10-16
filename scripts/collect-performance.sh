#!/usr/bin/env bash
# Run on the Linux CLIENT; measurements only against the lab VPN server.
set -euo pipefail
scenario=${1:-sin-qos}
[[ $scenario =~ ^[a-zA-Z0-9_-]+$ ]] || { echo "Nombre de escenario inválido" >&2; exit 1; }
target=10.77.0.1
out="resultados/rendimiento-${scenario}-$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$out"
# Two iperf3 servers must be running on the VPN server (5201 and 5202).
iperf3 -c "$target" -p 5201 -R -t 30 -J > "$out/normal.json" &
bulk_pid=$!
iperf3 -c "$target" -p 5202 -R -t 30 -J > "$out/prioritario.json" &
priority_pid=$!
ping -c 30 -i 1 "$target" > "$out/ping.txt" &
ping_pid=$!
status=0
wait "$bulk_pid" || status=1
wait "$priority_pid" || status=1
wait "$ping_pid" || status=1
printf 'Escenario: %s\nUTC: %s\nEstado: %s\n' "$scenario" "$(date -u --iso-8601=seconds)" "$status" > "$out/manifest.txt"
echo "Evidencia: $out (estado $status). Repita con y sin QoS al menos 3 veces."
exit "$status"
