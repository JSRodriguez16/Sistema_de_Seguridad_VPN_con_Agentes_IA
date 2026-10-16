# Sistema de seguridad VPN con agente IA

Prototipo académico sencillo: **WireGuard + agente Python + Random Forest + QoS DSCP/HTB + diagnóstico exportable** (no necesita API de IA, servicios de nube ni GPU).

El análisis y la demo funcionan en Windows y Linux. **El túnel real, la captura y QoS requieren un servidor Linux**. En este equipo se verificaron el procesamiento, entrenamiento, reportes y pruebas automatizadas; no se ha activado una VPN ni medido QoS real.

## 1. Ver resultados ahora, en Windows

Desde la raíz del proyecto, PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m vpn_guard demo --output resultados/mi-demo
Start-Process resultados/mi-demo/reporte.html
```

La demo **genera metadatos artificiales; no envía paquetes ni crea una VPN**. Entrena con 384 ventanas de 48 corridas y evalúa 128 ventanas de otras 16 corridas. Incluye navegación, transferencia legítima, escaneo y escaneo lento mezclado con actividad normal. Las fechas Unix sintéticas son fijas para reproducibilidad. Sus métricas no se presentan como resultados experimentales reales.

Ya hay una ejecución comprobada en `resultados/demo-verificada/reporte.html`. Las dependencias exactas verificadas están en `requirements-verified.txt`; `requirements.txt` permite instalar versiones compatibles en Linux.

## 2. Qué hace el sistema

El acceso inicial se limita a servicios del propio servidor (`10.77.0.1/32`). No requiere NAT ni reenvío IP; no cambia la ruta de Internet del cliente. Esto mantiene el laboratorio pequeño. Ampliarlo a otras subredes requeriría rutas y políticas de forwarding explícitas.

- WireGuard realiza autenticación por claves, intercambio Curve25519, cifrado autenticado ChaCha20-Poly1305 y BLAKE2s; Python no implementa criptografía propia.
- El agente cuenta paquetes, bytes, tasas, tamaños, intervalos, actividad observada, puertos/destinos únicos y proporciones SYN/RST/dirección.
- Random Forest clasifica normal/anomalía. Las reglas detectan muchos puertos o volumen elevado. El informe evalúa IA, reglas y la combinación por separado.
- Las alertas son observacionales: no bloquean automáticamente dispositivos. Transferencias legítimas pueden disparar la regla de volumen.
- QoS prioriza ICMP, respuestas SSH y el servicio de ensayo TCP 5202 sobre el resto de la **salida del servidor por wg0**, con un techo configurable.

**Visibilidad:** la captura en `wg0` ve cabeceras internas después de terminar el túnel. En la interfaz física se observa UDP cifrado y no los puertos internos. No se realiza inspección de contenido ni se guardan PCAP por defecto. Las IP y tiempos sí son metadatos del laboratorio; los resultados se guardan localmente.

## 3. Montar la VPN real

Use una VM Ubuntu/Debian como servidor y uno o dos clientes, en una red de laboratorio alcanzable. Asigne al servidor una IP accesible desde el cliente. Si está detrás de NAT, el reenvío UDP del router es un paso externo. No use `localhost` como endpoint desde otro equipo.

En el servidor ejecute:

```bash
bash scripts/install-linux.sh
# Sustituir 192.168.56.10 por la IP real del servidor.
.venv/bin/python -m vpn_guard init-vpn --endpoint 192.168.56.10:51820 --clients 2 --output private
sudo install -m 600 private/wg0.conf /etc/wireguard/wg0.conf
sudo wg-quick up wg0
```

`init-vpn` usa `wg genkey`/`wg pubkey`; guarda archivos privados con permisos 600 y directorio 700 en Linux. No muestra claves. `private/lab.json` contiene el inventario correspondiente. Use `--config private/lab.json` antes del subcomando en los comandos posteriores. Con dos clientes y valores predeterminados coincide con `config/lab.json`.

Transfiera `private/cliente-1.conf` por un medio privado al cliente. Importe el archivo con la aplicación oficial WireGuard en Windows, o en un cliente Linux:

```bash
sudo install -m 600 cliente-1.conf /etc/wireguard/wg0.conf
sudo wg-quick up wg0
ping -c 4 10.77.0.1
```

El firewall existente del servidor debe permitir UDP 51820 y los servicios de laboratorio sobre `wg0`. Por ejemplo, **si ya usa UFW**, ajuste sus reglas de UDP y acceso por `wg0`; no desactive el firewall. Las herramientas no cambian automáticamente esas reglas ni las del router.

Diagnóstico en el servidor:

```bash
sudo .venv/bin/python -m vpn_guard doctor --output resultados/estado-inicial.json
sudo wg show wg0 latest-handshakes
sudo wg show wg0 transfer
```

Nunca comparta `wg showconf`, `wg show ... dump` ni los `.conf` privados. El agente consulta únicamente campos sin claves secretas. Para revocar un dispositivo quite su sección `[Peer]` del servidor y aplique la configuración; las claves públicas autorizadas y `AllowedIPs` /32 son el control de acceso.

Para detener el laboratorio: `sudo wg-quick down wg0` en ambos extremos. Para arranque automático opcional: `sudo systemctl enable wg-quick@wg0` después de verificar la configuración.

## 4. Capturar, entrenar y evaluar tráfico real

Primero se necesitan capturas etiquetadas de su propio laboratorio. No se descargó ni simuló un dataset real. Sin `--model`, el agente ejecuta reglas y recolecta datos; el reporte dice **sin modelo IA**.

```bash
# Servidor, durante actividad normal del cliente de ensayo:
sudo .venv/bin/python -m vpn_guard monitor --seconds 120 --label normal --scenario navegacion --output resultados/normal-train
# Otra corrida: durante un escaneo controlado, descrito en docs/VALIDACION.md:
sudo .venv/bin/python -m vpn_guard monitor --seconds 120 --label anomaly --scenario escaneo --output resultados/scan-train
```

Repita **nuevas corridas** como `normal-test` y `scan-test`. Use un solo cliente activo durante una captura etiquetada: `--label` se aplica a todas las ventanas de esa corrida. El escenario debe sostenerse durante la captura; no etiquete minutos normales como ataque porque al final hubo un escaneo. Sin verdad de terreno use `monitor` sin `--label`.

```bash
.venv/bin/python -m vpn_guard train \
  --train resultados/normal-train/ventanas.csv resultados/scan-train/ventanas.csv \
  --test resultados/normal-test/ventanas.csv resultados/scan-test/ventanas.csv \
  --output resultados/modelo-real

sudo .venv/bin/python -m vpn_guard monitor --seconds 600 \
  --model resultados/modelo-real/modelo.joblib --output resultados/operacion-01
```

El modelo requiere al menos 20 ventanas de entrenamiento y ambas clases. La normalización se ajusta solamente sobre entrenamiento. Los `run_id` de entrenamiento y prueba deben ser distintos; ventanas vecinas de una misma captura permanecen juntas. Conserve los ID al reextraer: cambiarlos para reutilizar una captura invalidaría la evaluación. Para ajustar umbrales reserve corridas de validación adicionales; no ajuste sobre las de prueba final.

El modelo de la demo está marcado `synthetic`. La captura real lo rechaza por defecto; `--allow-demo-model` permite exploración explícita y muestra la advertencia en el informe. Para resultados defendibles entrene con tráfico real.

La captura continua usa `tshark`, excluye las ventanas parciales inicial/final y registra pérdidas, campos inválidos y paquetes tardíos. Las ventanas sin tráfico no se inventan. La cola está acotada; revise sus descartes antes de confiar en los resultados. Durante captura aparecen alertas en consola y `alertas_en_vivo.jsonl`; al finalizar se genera el HTML. `Ctrl+C` intenta cerrar la corrida y preservar evidencias. El proceso tiene una duración máxima explícita para controlar el tamaño de los archivos.

Solo cargue archivos `.joblib` generados por usted: este formato puede ejecutar código al deserializar. El laboratorio ejecuta captura con sudo por simplicidad; un despliegue permanente debería separar privilegios de captura e inferencia.

## 5. Diagnosticar los resultados

Abra `reporte.html` de cada corrida; no necesita servidor web ni conexión a Internet.

| Archivo | Uso |
|---|---|
| `metricas.json` | TP, FP, TN, FN; accuracy, precision, recall, F1 y FPR; métricas por escenario |
| `predicciones.csv` | Todas las ventanas, atributos, probabilidad, reglas y decisión final |
| `errores.csv` | Falsos positivos y falsos negativos del detector combinado |
| `alertas.jsonl` | Alertas completas para trazabilidad |
| `ventanas.csv` / `paquetes.csv` | Características y metadatos de una captura real |
| `manifest.json` | Corrida, etiqueta, parámetros, duración y errores operativos |
| `estado_vpn.jsonl` / `eventos_vpn.jsonl` | Endpoints, bytes, estado de handshake y cambios observados |
| `captura.stderr.log` | Errores y estadísticas que reporta tshark |
| `modelo_metadata.json` | Semilla, versiones, clases, corridas y relevancia global de características |

**FP**: tráfico normal marcado; revise volumen legítimo y puertos concurrentes. **FN**: anomalía no marcada; revise escaneos lentos, ventana y representatividad del entrenamiento. **FPR = FP / (FP + TN)**. Sin etiquetas no se calcula accuracy; una razón con denominador cero aparece como `null`/«No calculable».

`inference_ms_p95` mide el cálculo por ventana; no incluye los 10 segundos de acumulación ni cola. CPU y memoria son del agente Python, no del kernel ni de tshark. La duración activa dentro de una ventana no es la duración de una sesión TCP. `recent`, `stale` y `never` describen el handshake; no son una prueba de conexión/desconexión. WireGuard silencioso no permite contar autenticaciones rechazadas ni identificar claves no autorizadas con estos comandos; las pruebas externas se documentan por separado.

## 6. QoS y mediciones de disponibilidad

Con `wg0` activo, servidor:

```bash
sudo bash scripts/qos.sh apply 10
sudo bash scripts/qos.sh status
# Restaurar el qdisc por defecto y quitar únicamente reglas de este proyecto:
sudo bash scripts/qos.sh remove
```

HTB limita la salida a 10 Mbit/s: clase prioritaria con 25% garantizado y clase normal con 75%; ambas pueden usar capacidad libre. La prioridad favorece el préstamo de capacidad, no elimina el mínimo normal. DSCP EF (46) identifica la clase prioritaria. Las reglas no reemplazan qdisc ajenos; el script falla si encuentra uno. La política no persiste tras reiniciar: reaplíquela después de levantar `wg0`.

Para medir, inicie **en dos terminales del servidor**:

```bash
iperf3 -s -B 10.77.0.1 -p 5201
iperf3 -s -B 10.77.0.1 -p 5202
```

En el cliente Linux, con los scripts copiados:

```bash
bash scripts/collect-performance.sh sin-qos
# Active QoS en el servidor y repita:
bash scripts/collect-performance.sh con-qos
```

Los dos ensayos `iperf3 -R` concurrentes miden servidor → cliente y `ping` registra latencia/pérdida. Repita al menos tres veces por condición; use el mismo tráfico y conserve `tc -s class show dev wg0` antes/después para comprobar bytes en ambas clases. Un límite solo será visible si hay suficiente carga. El DSCP interno no garantiza priorización en routers externos.

```bash
.venv/bin/python -m vpn_guard performance \
  --input resultados/rendimiento-sin-qos-*/*.json --output resultados/resumen-sin-qos
.venv/bin/python -m vpn_guard performance \
  --input resultados/rendimiento-con-qos-*/*.json --output resultados/resumen-con-qos
```

El resumen produce Mbps medio, desviación, retransmisiones y datos UDP si existen. No convierte ausencia de datos en cero. En PowerShell use rutas explícitas, pues los comodines no se expanden para Python como en Bash.

## 7. Verificación y documentación

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m vpn_guard --help
```

- [Validación controlada y tabla de evidencias](docs/VALIDACION.md)
- [Decisiones y relación con las referencias](docs/DISENO.md)
- [Verificación realizada y pruebas pendientes](docs/VERIFICACION.md)

`documentacion/` ya estaba excluida por `.gitignore`; se conserva esa decisión. Las guías nuevas están en `docs/` para poder versionarlas. Las claves, capturas, modelos y resultados están excluidos. El `.tex` original no se rellenó con resultados sintéticos.
