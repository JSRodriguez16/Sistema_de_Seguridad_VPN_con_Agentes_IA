# Verificación local del prototipo

Fecha: 16 de octubre de 2026, zona America/Bogota. Entorno: Windows, Python 3.14.5. Versiones de dependencias en `requirements-verified.txt`.

## Comprobado

- 22 pruebas automatizadas con `python -m unittest discover -s tests -v`: extracción bidireccional, intervalos y límites de ventanas, escaneo entre flujos, errores de entrada, parsing tshark, separación de corridas, normalización solo en entrenamiento, serialización, independencia de identificadores, datos duplicados, métricas y casos sin etiquetas, reportes, ciclo de captura con procesos simulados, configuración WireGuard, snapshots sin secretos y resumen iperf3.
- Demo, entrenamiento desde CSV, evaluación independiente, análisis con solo reglas, extracción desde paquetes, ayuda CLI y diagnóstico de entorno ejecutados.
- `pip check`: sin dependencias incompatibles. Compilación Python correcta. Sintaxis Bash comprobada en los tres scripts usando Bash de Git para Windows.
- Reportes HTML y exportaciones JSON/CSV generados. El navegador conectado no está disponible en esta sesión; no se afirma inspección visual del HTML en un navegador.

## Evidencia sintética conservada localmente

- `resultados/demo-verificada/`: 384 ventanas de entrenamiento y 128 de prueba, 48/16 corridas independientes, semilla 42.
- `resultados/evaluacion-verificada/`: reevaluación del modelo guardado.
- `resultados/entrenamiento-verificado/`: entrenamiento/evaluación a partir de los CSV guardados.
- `resultados/reglas-verificadas/`: baseline sin IA sobre las mismas ventanas de prueba.
- `resultados/extraccion-verificada.csv`: 32 ventanas reextraídas de metadatos artificiales, solo para verificar el extractor.
- `resultados/diagnostico-entorno.json`: ausencia de las herramientas de red requeridas en este Windows.

En esta demo el sistema combinado obtuvo TN=64, FP=0, FN=0, TP=64. Las reglas solas obtuvieron TN=64, FP=0, FN=32, TP=32. **Estos valores caracterizan únicamente el generador sintético**. No prueban generalización, protección ni ventaja real de IA. La separación por corrida evita mezclar ventanas vecinas pero todos estos datos siguen saliendo del mismo generador artificial.

## Pendiente en equipos Linux reales

Activación WireGuard, conectividad entre equipos, rechazo/revocación de claves, captura tshark sobre `wg0`, carga real, comportamiento del kernel y de `tc`/iptables, aplicación y reversión efectiva de QoS y comparación de rendimiento. Los tests de captura y WireGuard usan dobles controlados; no sustituyen estas pruebas.

Siga `VALIDACION.md` y conserve cada evidencia antes de escribir resultados experimentales en el artículo.
