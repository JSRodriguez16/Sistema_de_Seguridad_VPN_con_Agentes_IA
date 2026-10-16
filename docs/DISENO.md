# Diseño y trazabilidad

## Alcance del anteproyecto

Fuentes locales revisadas: `documentacion/conference_101719.tex`; las tres páginas escaneadas de `EntregaAnteproyectoFinal.pdf`, porque `EntregaAnteproyectoFinal.md` tiene cero bytes; y las cinco referencias `.md` de `documentacion/Referencias/`.

| Requisito | Implementación | Evidencia/limitación |
|---|---|---|
| VPN cliente-servidor, pocos dispositivos | `init-vpn`, WireGuard Linux y clientes nativos | Generación por `wg`; requiere activar en equipos reales |
| Confidencialidad, integridad, autenticidad | Primitivas nativas de WireGuard | No hay una implementación criptográfica casera |
| Autorización por claves | `[Peer]` y `AllowedIPs` /32 por cliente | Cliente limitado a IP del servidor en este MVP |
| IP, dispositivos, conexiones y tiempos | Inventario, metadatos, snapshots y eventos de handshake | No hay sesiones de conexión persistentes ni auditoría exhaustiva de rechazos en WireGuard |
| Monitoreo periódico y alertas IA | Captura continua + ventanas de 10 s + bosque de 100 árboles | Clasificación binaria entrenada con etiquetas; no reconoce cualquier ataque desconocido |
| Disponibilidad, DSCP y TC/HTB | `scripts/qos.sh`, clases de salida y contadores | Solo salida IPv4 del servidor; no policer de subida ni garantía en Internet |
| Diagnosticar efectividad | Holdout por corrida, métricas, errores, inferencia y recursos | Las métricas necesitan etiquetas independientes verificadas |
| Ensayos de rendimiento | iperf3 concurrente + ping + resumen JSON/CSV | Es necesario ejecutarlos en red; no se han inventado mediciones |

## Cómo se usaron las cinco referencias

1. **Real Time VPN Traffic Attack Detection and Classification**: aporta WireGuard, laboratorio de escaneo, metadatos de flujo, Random Forest y evaluación por corrida. Se conserva RF y el escenario de reconocimiento; se omiten XGBoost y la etapa multiclase para mantener el alcance. El propio trabajo distingue resultados offline de una prueba en vivo con accuracy de 75%; sus porcentajes no se transfieren a este prototipo.
2. **Intelligent VPN Traffic Analysis and Classification Framework on Raspberry Pi Using Machine Learning Techniques**: guía la arquitectura compacta y el procesamiento local. Se usa un único modelo clásico con profundidad limitada y un hilo. No se implementa TensorFlow Lite: el artículo trata RF/SVM y una red neuronal convertida por separado; no se supone una conversión automática de RF a TFLite.
3. **VPN-Encrypted Network Traffic Classification Using a Time-Series Approach**: guía ventanas temporales, tamaño, dirección e intervalos. Aquí son ventanas contiguas de 10 s por peer, sin solapamiento, con estadísticos; no se afirma reproducir InceptionTime ni sus ventanas de 60 s ni clasificación de aplicaciones.
4. **Network Traffic Classification Using Self-Supervised Learning and Confident Learning**: motiva controlar la calidad de etiquetas y usar atributos sin payload. Este MVP requiere etiquetas verificadas; no produce pseudoetiquetas ni implementa SSL/CL. Una decisión del modelo no se usa como verdad de terreno para evaluar ese mismo modelo.
5. **DarkDetect: Darknet Traffic Detection and Categorization**: guía las métricas por clase, manejo del desbalance y selección de atributos. Se usa `class_weight=balanced`; no se implementan CNN-LSTM, SMOTE ni clasificación de darknets. No se equipara «tráfico VPN» a «malicioso».

Estos son referentes metodológicos, no código reutilizado ni reproducciones exactas. Los `.md` contienen extracciones con tablas deformadas e incluso afirmaciones ambiguas; se tomaron decisiones explícitas para evitar trasladarlas sin revisión.

## Variables y decisiones

Una observación representa un **peer durante una ventana**, agregando múltiples conexiones. Esto permite contar los destinos/puertos de un escaneo; un flujo individual de cinco campos tendría casi siempre un solo puerto de destino.

| Característica | Definición |
|---|---|
| packets, bytes | Conteos bidireccionales de paquetes IPv4 y `ip.len` interno |
| packets_per_second, bytes_per_second | Conteo dividido por duración configurada, incluso si solo hubo actividad breve |
| mean/std_packet_bytes | Media y desviación poblacional del tamaño IPv4 |
| mean/std_iat_ms | Media y desviación entre paquetes consecutivos del peer dentro de la ventana |
| active_seconds | Último menos primer timestamp observado |
| unique_dst_ports, unique_dst_ips | Destinos del tráfico originado por el peer; puertos de retorno no cuentan |
| syn_ratio | SYN sin ACK salientes / paquetes salientes |
| rst_ratio | Paquetes con RST / total bidireccional |
| outbound_ratio | Paquetes originados por peer / total bidireccional |

Las IP, los nombres, el timestamp, la etiqueta y el escenario se conservan para diagnóstico pero **no son entradas del modelo**. Se rechazan valores inválidos/NaN/infinito en lugar de entrenar silenciosamente con datos rotos. Los momentos se calculan incrementalmente; la memoria no depende de guardar cada tamaño/intervalo. Los destinos únicos se saturan en 4096; los puertos están acotados por 65535. Si hay tráfico entre dos peers ambos se contabilizan; no sume sus bytes como volumen global sin deduplicar.

StandardScaler implementa `(x - media) / desviación` ajustado únicamente en entrenamiento. Aunque RF no necesita normalización para comparar umbrales, se mantiene como etapa explícita del anteproyecto. RF usa 100 árboles, profundidad 8, hoja mínima 2, semilla 42 y un hilo. El umbral predeterminado de voto/probabilidad es 0.65; no es una probabilidad calibrada ni una certeza de intrusión.

La política final es `alerta_modelo OR alerta_regla`. Regla 1: al menos 20 puertos destino por ventana. Regla 2: al menos 1 MB/s agregado. Son parámetros de partida, no umbrales universalmente válidos. El volumen alto no se etiqueta automáticamente como DDoS. El informe muestra métricas separadas para impedir atribuir a IA lo que hizo una regla.

Las referencias clasifican tráfico o ataques conocidos; este RF supervisado necesita ejemplos representativos normales y anómalos. No se presenta como detector universal de novedades. Escaneos muy lentos, cambios de aplicaciones y actividad fuera del inventario/IPv4 son limitaciones concretas.

## Fuentes técnicas oficiales consultadas

- [WireGuard: configuración y generación de claves](https://www.wireguard.com/quickstart/).
- [WireGuard: protocolo y primitivas criptográficas](https://www.wireguard.com/protocol/).
- [Wireshark: tshark y exportación de campos](https://www.wireshark.org/docs/man-pages/tshark.html).
- [scikit-learn: RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).
- [scikit-learn: evitar fuga de datos con pipelines](https://scikit-learn.org/stable/common_pitfalls.html).
- [Manual Linux de TC/HTB](https://man7.org/linux/man-pages/man8/tc-htb.8.html).
