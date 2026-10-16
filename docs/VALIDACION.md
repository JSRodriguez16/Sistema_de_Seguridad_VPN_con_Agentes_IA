# Plan de validación y diagnóstico experimental

## Preparación

Use dos equipos/VM: servidor Linux y cliente autorizado. Un tercer cliente es opcional. Verifique que UDP 51820 sea alcanzable; registre versiones, IP de cada interfaz, CPU, RAM, MTU y enlaces. Sincronice los relojes. Mantenga el resto del entorno estable. Las órdenes siguientes son exclusivamente para el servidor propio `10.77.0.1` del laboratorio.

La demo no valida cifrado, autenticación, rendimiento ni QoS. La verificación local de Python usa paquetes sintéticos y dobles de comandos WireGuard. El servidor Linux aún requiere las pruebas de esta guía.

## 1. Protección del túnel y autorización

1. Con el peer registrado, active ambos túneles y haga `ping 10.77.0.1`. Guarde `doctor`, fecha e IPs. Compruebe handshake reciente y contadores que aumentan.
2. Observe en la interfaz física del servidor con una herramienta local de captura que el transporte es UDP al puerto configurado. Compare con las cabeceras internas que ve en `wg0`. Conservar metadatos externos sirve como evidencia de encapsulación, no demuestra por sí solo toda la seguridad criptográfica.
3. En un tercer perfil de ensayo use una clave pública no registrada, con la misma IP cliente pero **sin activar simultáneamente el perfil válido**. Intente llegar únicamente a `10.77.0.1`. Conserve el intento del cliente, ausencia de handshake y ausencia de paquetes internos correspondientes. Reactive el perfil válido y compruebe recuperación. Nunca publique claves privadas.
4. Si revoca el peer válido, verifique que pierde el acceso. No confunda un fallo por firewall/ruta con una prueba exitosa de autenticación: el control positivo válido debe funcionar bajo las mismas condiciones.

Los intentos inválidos ocurren antes de `wg0`; el agente no les puede atribuir identidad ni contarlos como autenticaciones rechazadas. Si necesita evidencia de recepción externa, use `sudo tcpdump -ni INTERFAZ_FISICA 'udp dst port 51820' -q` y guarde la salida textual durante el ensayo. Esto cuenta tráfico UDP, no fallos de autenticación. No se habilita logging de depuración del kernel ni se promete trazabilidad que WireGuard no expone.

## 2. Tráfico normal y anomalías controladas

Normal: ping, navegación a un servicio propio, SSH y transferencia legítima. Para un servicio mínimo en el servidor, abra una carpeta de prueba que solo contenga datos públicos y ejecute `python3 -m http.server 8080 --bind 10.77.0.1`; consúmalo desde el cliente. No sirva la raíz de este repositorio, que podría contener `private/`.

Escaneo: instale `nmap` en el cliente Linux del laboratorio. Antes de iniciar la captura, sostenga un ensayo acotado de unos minutos contra su servidor:

```bash
# Solo sobre el servidor propio de este laboratorio. Sin explotación.
for i in 1 2 3 4; do
  nmap -sT -Pn -n --max-rate 20 --max-retries 0 -p 1-1024 10.77.0.1
done
```

Capture 120 s mientras el escenario está activo. `--label anomaly` significa que el escenario anómalo estuvo presente en esas ventanas; no que todos los paquetes sean ataques. Mantenga el otro peer sin tráfico. Use `--max-rate 2` para probar un reconocimiento más lento y documente su duración real; puede atravesar pocas puertas por ventana y eludir la regla. Detenga la prueba al terminar su ventana de laboratorio.

Genere al menos tres corridas independientes normales y tres anómalas para entrenamiento, y nuevas corridas para prueba final. Cambie hora, ritmos y servicios dentro del alcance. Incluya transferencias legítimas grandes para medir falsos positivos. Es útil reservar otras corridas para ajustar parámetros antes de congelar el modelo.

No mezcle ventanas contiguas de la misma corrida en train/test, no renombre una captura para eludir el control, no entrene con los resultados finales y no use predicciones como etiquetas. Si una captura mezcla periodos sin etiquetado preciso, úsela para observación o anote/revise las etiquetas por ventana antes de entrenar.

## 3. Evaluación del detector

Con el modelo congelado, evalúe otra captura etiquetada:

```bash
.venv/bin/python -m vpn_guard evaluate --model resultados/modelo-real/modelo.joblib \
  --input resultados/normal-final/ventanas.csv resultados/scan-final/ventanas.csv \
  --output resultados/evaluacion-final
```

Revise `errores.csv` fila por fila y compare con el manifiesto del ensayo. Informe el número de ventanas por clase y sus corridas, no solo porcentajes. Una matriz con cero FP en una muestra pequeña no implica ausencia de falsas alarmas futuras. Reporte IA, reglas y combinación; compare con la regla simple como baseline. Una reducción de FP puede aumentar FN al subir el umbral.

Mida el tiempo desde comienzo del escenario hasta primera alerta a partir de timestamps y registros del ensayo. La inferencia p95 es solo cómputo; el retardo real incluye acumulación de ventana, cola y captura. Revise descartes, filas inválidas y errores de tshark; evidencia incompleta debe identificarse.

## 4. QoS y disponibilidad

Siga los comandos iperf3 del README. Mida tres o más repeticiones sin QoS y tres o más con QoS; compare Mbps de ambos servicios, ping medio/máximo, pérdida y retransmisiones. Conserve las salidas `tc -s class show dev wg0` y `iptables -t mangle -L VPNGUARD_QOS -nv`. Debe haber bytes en clases 77:10 y 77:20 cuando los dos servicios transfieren.

QoS afecta solo al egreso de `wg0` del servidor: utilice `iperf3 -R` en el cliente. Una prueba de subida no valida esta política. Si el enlace real ya limita por debajo del techo HTB, es posible no ver cambios. No presente un techo de ancho de banda como evidencia de mayor disponibilidad sin comparar también latencia/pérdida bajo carga.

## Tabla para redactar resultados en el .tex

| Experimento | Corridas/datos | Evidencia que debe conservarse | Resultado actual |
|---|---|---|---|
| Demo software | Sintético, train/test separados | reporte, métricas, modelo y semilla | Generado localmente; no resultado de VPN |
| Acceso autorizado | Cliente válido | Ping, handshake, bytes, manifiesto | Pendiente en Linux |
| Clave no registrada/revocada | Control positivo y negativo | Intento cliente, estado y recepción UDP externa | Pendiente en Linux |
| Encapsulación | Captura externa vs wg0 | Metadatos y configuración sin secretos | Pendiente en Linux |
| Normal / scan / slow scan | Capturas reales etiquetadas | Confusión, FP/FN, predicciones, etiquetas | Pendiente en Linux |
| Costo del agente | Misma carga con/sin agente | CPU, RSS, retardo y throughput | Pendiente en Linux |
| QoS | ≥3 repeticiones por condición | iperf3 JSON, ping y contadores TC | Pendiente en Linux |

Los apartados de resultados y conclusiones del `.tex` permanecen para evidencia real. Al redactarlos indique topología, versiones, tamaños de muestra, split, parámetros, unidades y limitaciones; no copie los porcentajes de las referencias ni la demo como si fueran mediciones de este túnel.
