#!/usr/bin/env bash
# Owns only wg0 egress qdisc 77: and the VPNGUARD_QOS mangle chain.
set -euo pipefail
action=${1:-status}
iface=wg0
rate=${2:-10}
chain=VPNGUARD_QOS
marker=/run/vpn-guard-qos-wg0
[[ $EUID -eq 0 ]] || { echo "Use sudo bash scripts/qos.sh ..." >&2; exit 1; }
[[ $action =~ ^(apply|remove|status)$ ]] || { echo "Uso: qos.sh apply [Mbit/s] | remove | status" >&2; exit 1; }
command -v tc >/dev/null
command -v iptables >/dev/null
ip link show dev "$iface" >/dev/null

remove_owned() {
  [[ -f $marker ]] || { echo "No hay política de este proyecto registrada."; return; }
  if iptables -t mangle -C OUTPUT -o "$iface" -j "$chain" 2>/dev/null; then
    iptables -t mangle -D OUTPUT -o "$iface" -j "$chain"
  fi
  if iptables -t mangle -S "$chain" >/dev/null 2>&1; then
    iptables -t mangle -F "$chain"
    iptables -t mangle -X "$chain"
  fi
  if tc qdisc show dev "$iface" | grep -q 'qdisc htb 77: root'; then
    tc qdisc del dev "$iface" root
  fi
  rm -f -- "$marker"
}

if [[ $action == remove ]]; then
  remove_owned
  exit
fi
if [[ $action == apply ]]; then
  [[ $rate =~ ^[0-9]{1,5}$ ]] && (( rate >= 4 && rate <= 10000 )) || { echo "Tasa entera entre 4 y 10000 Mbit/s" >&2; exit 1; }
  existing=$(tc qdisc show dev "$iface")
  if ! [[ $existing == *"qdisc noqueue"* || ( -f $marker && $existing == *"qdisc htb 77: root"* ) ]]; then
    echo "Existe otro qdisc raíz; no se reemplaza. Revise: tc qdisc show dev wg0" >&2
    exit 1
  fi
  if iptables -t mangle -S "$chain" >/dev/null 2>&1 && [[ ! -f $marker ]]; then
    echo "La cadena $chain ya existe sin marca de propiedad." >&2
    exit 1
  fi
  remove_owned
  touch "$marker"
  trap 'remove_owned' ERR
  priority=$((rate / 4))
  standard=$((rate - priority))
  tc qdisc replace dev "$iface" root handle 77: htb default 20
  tc class add dev "$iface" parent 77: classid 77:1 htb rate "${rate}mbit" ceil "${rate}mbit"
  tc class add dev "$iface" parent 77:1 classid 77:10 htb rate "${priority}mbit" ceil "${rate}mbit" prio 0
  tc class add dev "$iface" parent 77:1 classid 77:20 htb rate "${standard}mbit" ceil "${rate}mbit" prio 1
  tc qdisc add dev "$iface" parent 77:10 handle 710: fq_codel
  tc qdisc add dev "$iface" parent 77:20 handle 720: fq_codel
  tc filter add dev "$iface" protocol ip parent 77: prio 1 u32 match ip tos 0xb8 0xfc flowid 77:10
  iptables -t mangle -N "$chain"
  # Reset existing DSCP before trusting the local service-based policy.
  iptables -t mangle -A "$chain" -j DSCP --set-dscp 0
  iptables -t mangle -A "$chain" -p icmp -j DSCP --set-dscp-class EF
  iptables -t mangle -A "$chain" -p tcp --sport 22 -j DSCP --set-dscp-class EF
  iptables -t mangle -A "$chain" -p tcp --sport 5202 -j DSCP --set-dscp-class EF
  iptables -t mangle -A OUTPUT -o "$iface" -j "$chain"
  trap - ERR
fi
tc -s class show dev "$iface"
tc -s qdisc show dev "$iface"
iptables -t mangle -L "$chain" -nv 2>/dev/null || true
echo "Alcance: salida IPv4 del servidor por wg0; no prioriza subida ni garantiza QoS en Internet."
