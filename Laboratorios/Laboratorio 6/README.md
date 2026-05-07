
Las señales fisiológicas son relevantes porque permiten registrar la actividad eléctrica del cuerpo humano, lo que posibilita el diagnóstico, seguimiento y evaluación en tiempo real del paciente; esto con la finalidad de obtener indicios sobre una posible afección o encontrar patrones que deriven en una enfermedad. Sin embargo, estas suelen tener una amplitud de entre microvoltios y milivoltios, lo que dificulta su recolección. El ruido aleatorio, las líneas eléctricas, la interferencia fisiológica, los artefactos de movimiento y la colocación incorrecta de los electrodos son solo algunos ejemplos de las diferentes fuentes de ruido.

Se han aplicado diversos métodos de procesamiento para obtener señales de electrocardiografía (ECG), electroencefalografía (EEG) y electromiografía (EMG). Entre estos destacan los filtros, que son redes o sistemas encargados de alterar la forma de onda, la amplitud-frecuencia y/o la fase-frecuencia de una señal. El filtrado se utiliza para mejorar la calidad del registro, extraer información o separar señales mixtas [1], considerando las frecuencias de onda propias de cada señal.

# Tipos de filtros digitales:

## Señales EMG:
### Pasa-banda Butterworth (IIR)
La señal de electromiografía de superficie (sEMG) presenta su contenido de frecuencias utiles principalmente entre 20 Hz y 400 Hz,la cual es donde se concentra la información asociada a la activación muscular.Sin embargo,esta señal suele estar contaminada por artefactos de movimiento (frecuencias menores a 20 Hz) y ruido de altas frecuencias que proviene del sistema electrónico.
Para mitigar estos efectos,se emplea un filtro pasa-banda tipo Butterworth,con frecuencias de corte entre 20 Hz y 450 Hz.Este filtro nos ayuda a eliminar tanto las componentes de baja frecuencia como las de alta frecuencia, conservando únicamente la banda de interés.
El filtro Butterworth su principal caracteristica es tener una respuesta en frecuencia plana en la banda de paso (bajo grado de oscilaciones en la banda de paso), lo que evita distorsionar la amplitud de la señal, siendo especialmente útil en el análisis de la señales musculares [2]

## Señales ECG:

## Señales EEG:
### Filtro pasa alto método de ventana de Hanning:
El parpadeo induce un artefacto de gran amplitud debido al movimiento del globo ocular generando cambios de potencial, se presenta como una señal de baja frecuencia, típicamente situada en el rango de 0.1 Hz a 10 Hz [3].
Para mitigar esta interferencia, se implementan filtros digitales de paso alto que permiten bloquear estas ondas lentas mientras se preservan las frecuencias superiores del EEG. El EEG clínico convencional se centra generalmente en ondas que van de 0,5 a 70 Hz [4]. En particular, el uso de la técnica de ventana de Hanning estabiliza la respuesta del filtro en un tiempo de 11.965 s en ondas theta (4 Hz a 8 Hz); facilito la eliminación del desplazamiento de la línea base provocado por el ojo y mejora la precisión en la detección de patrones críticos, como las crisis epilépticas [5,6].

## Generales:

### Notch (Rechaza-banda)
Para la adquision de señales sEMG, ECG y EEG es común la presencia de interferencia de la red eléctrica,la cual introduce una componente sinusoidal 60 Hz, si hablamos del territorio peruano.
Para eliminar este tipo de ruido, se utiliza un filtro notch (rechaza-banda),diseñado para atenuar una banda muy estrecha de frecuencias centradas en 60 Hz. Este filtro permite suprimir la interferencia eléctrica sin afectar significativamente el resto del contenido de espectros de la señal biomédica.[1]
 
## Bibliografia 
[1]
[2] D. Pradon, L. Tong, C. Chalitsios, y N. Roche, “Development of surface EMG for gait analysis and rehabilitation of hemiparetic patients”, Sensors (Basel), vol. 24, núm. 18, p. 5954, 2024.
[3] A. Pant y A. Kumar, "Exploración del procesamiento de señales EEG para el filtrado y la clasificación eficaces de crisis epilépticas," Discov. Electron., vol. 3, no. 20, 2026. [En línea]. Disponible en: https://doi.org/10.1007/s44291-026-00174-2
[4] C. S. Nayak y A. C. Anilkumar, "EEG Normal Waves,"StatPearls. Treasure Island, FL, USA: StatPearls Publishing, 2026. [En línea]. Disponible en: https://www.ncbi.nlm.nih.gov/books/NBK539805/ 
[5] A. Pant y A. Kumar, "Hanning FIR window filtering analysis for EEG signals," Biomedical Analysis, vol. 1, no. 2, pp. 111-123, Jun. 2024, doi: 10.1016/j.bioana.2024.05.003.
[6] A. Pant, A. Kumar, C. Verma, y Z. Illés, "Comparative exploration on EEG signal filtering using window control methods," Results in Control and Optimization, vol. 17, art. 100485, dic. 2024, doi: 10.1016/j.rico.2024.100485.
