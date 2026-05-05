## Filtro 1: Pasa-banda Butterworth (IIR)
La señal de electromiografía de superficie (sEMG) presenta su contenido de frecuencias utiles principalmente entre 20 Hz y 400 Hz,la cual es donde se concentra la información asociada a la activación muscular.Sin embargo,esta señal suele estar contaminada por artefactos de movimiento (frecuencias menores a 20 Hz) y ruido de altas frecuencias que proviene del sistema electrónico.
Para mitigar estos efectos,se emplea un filtro pasa-banda tipo Butterworth,con frecuencias de corte entre 20 Hz y 450 Hz.Este filtro nos ayuda a eliminar tanto las componentes de baja frecuencia como las de alta frecuencia, conservando únicamente la banda de interés.
El filtro Butterworth su principal caracteristica es tener una respuesta en frecuencia plana en la banda de paso (bajo grado de oscilaciones en la banda de paso), lo que evita distorsionar la amplitud de la señal, siendo especialmente útil en el análisis de la señales musculares [1]







## Bibliografia 
[1]D. Pradon, L. Tong, C. Chalitsios, y N. Roche, “Development of surface EMG for gait analysis and rehabilitation of hemiparetic patients”, Sensors (Basel), vol. 24, núm. 18, p. 5954, 2024.
