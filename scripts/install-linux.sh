#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ $EUID -eq 0 ]]; then
  echo "Ejecute como usuario normal con sudo disponible para apt, no como root." >&2
  exit 1
fi
sudo apt-get update
# tshark can ask whether non-root users may capture; answer No for this lab.
sudo apt-get install -y wireguard-tools tshark iproute2 iptables iperf3 python3-venv
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
echo "Dependencias instaladas. Continúe con README.md; todavía no se ha activado ninguna VPN."
