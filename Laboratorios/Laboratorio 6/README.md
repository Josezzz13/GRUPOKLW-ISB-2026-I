<img width="350" height="190" alt="hq720" src="https://github.com/user-attachments/assets/8e54ecf8-3a98-43ab-8ea1-550641973c17" />

# Laboratorio 6: Filtros digitales aplicados a señales biomédicas.

Las señales fisiológicas permiten registrar la actividad eléctrica del cuerpo humano, lo que posibilita el diagnóstico, seguimiento y evaluación en tiempo real del paciente; esto con la finalidad de obtener indicios sobre una posible afección o encontrar patrones que deriven en una enfermedad. Para captarlas se emplean conductores eléctricos denominados electrodos invasivos/intramusculares o electrodos de superficie basándose en el principio de transducción electroquímica, convirtiendo las corrientes iónicas producidas por las células del cuerpo en corrientes de electrones que pueden ser medidas.

*Figura 1. Interfaz típica cuerpo-electrodo: la corriente iónica en el cuerpo se convierte en corriente electrónica y viceversa en la interfaz [1].* 
<img width="600" height="300" alt="Captura de pantalla 2026-05-08 193011" src="https://github.com/user-attachments/assets/613365cb-231a-41a6-b773-a2f05b14a4c2" />

Tras su obtención las señales presentan una amplitud de entre microvoltios y milivoltios, lo que dificulta su visualización e interpretación, ya que puede presentar ruido, oscilaciones producto de las líneas eléctricas, la interferencia fisiológica como movimientos involuntarios o artefactos y de la colocación incorrecta de los electrodos. Para una correcta evaluación y mitigar la presencia de ruido, se han aplicado diversos métodos de procesamiento para obtener señales de electrocardiografía (ECG), electroencefalografía (EEG) y electromiografía (EMG). Entre estos destacan los filtros, que son redes o sistemas que impiden el paso de frecuencias identificadas ruido o no propias del rango propio de la señal, sin alterar la forma de onda, la amplitud-frecuencia y/o la fase-frecuencia de una señal como en el caso de ECG el rango de frecuencia que proporciona información va desde 0.5 Hz a 150 Hz, en el caso del EMG de 5 Hz a 500 Hz y EEG correspondiente que va desde 0.5 Hz a 70 Hz.

A continuación se mencionará diferentes tipos de filtros empleados por las 3 señales mencionadas.

## Tipos de filtros digitales:

### Señales EMG:

#### Pasa-banda Butterworth (IIR)
La señal de electromiografía de superficie (sEMG) presenta su contenido de frecuencias utiles principalmente entre 20 Hz y 400 Hz,la cual es donde se concentra la información asociada a la activación muscular.Sin embargo,esta señal suele estar contaminada por artefactos de movimiento (frecuencias menores a 20 Hz) y ruido de altas frecuencias que proviene del sistema electrónico.
Para mitigar estos efectos,se emplea un filtro pasa-banda tipo Butterworth,con frecuencias de corte entre 20 Hz y 450 Hz.Este filtro nos ayuda a eliminar tanto las componentes de baja frecuencia como las de alta frecuencia, conservando únicamente la banda de interés.
El filtro Butterworth su principal caracteristica es tener una respuesta en frecuencia plana en la banda de paso (bajo grado de oscilaciones en la banda de paso), lo que evita distorsionar la amplitud de la señal, siendo especialmente útil en el análisis de la señales musculares [2]

### Señales ECG:

### Señales EEG:

Es una prueba que mide la actividad eléctrica del cerebro, permite detectar cambios en la actividad cerebral que podrían ayudar a diagnosticar afecciones cerebrales, especialmente epilepsia u otras afecciones afines. También puede servir para confirmar la muerte cerebral en alguien que se encuentra en estado de coma[eeg1].
Los electrodos de EEG se colocan sobre o alrededor de los músculos craneales como se muestra en la figura ee2.

*Figura e2. Sistema Internacional 10-20 para la colocación de los electrodos extracraneales. Las letras señalan el área (Fp, prefrontal; F, frontal; C, central; P, parietal; T, temporal y O, occipital), mientras que los números designan el hemisferio (pares del derecho, nones del izquierdo) y los electrodos de la línea media se señalan con una "z"; por lo que Fz se encuentra frontalmente en la línea media [eeg2].*

<img width="600" height="400" alt="Captura de pantalla 2026-05-08 215208" src="https://github.com/user-attachments/assets/e52b698b-5a79-4805-b7a2-334f81da1255" />


Al estar ubicado en la cabeza, la actividad miogénica del frontal, el temporal, los músculos oculares, los músculos del cuello y los músculos periauriculares pueden interferir con la señal de EEG registrada [eeg3]. Todo ello genera ruido por, principalmente, diafonía entre sitios de registro cercanos, para ello se emplean los siguientes filtros:

#### Pasa altos método de ventana de Hanning:

El parpadeo induce un artefacto de gran amplitud debido al movimiento del globo ocular, generando cambios de potencial; este se presenta como una señal de baja frecuencia, típicamente situada en el rango de 0.1 Hz a 10 Hz [eeg4]. Para mitigar esta interferencia, se implementan filtros digitales de paso alto que permiten bloquear estas ondas lentas mientras se preservan las frecuencias superiores del EEG. El EEG clínico convencional se centra, generalmente, en ondas que van de 0.5 a 70 Hz [eeg5].
El uso de la técnica de ventana de Hanning estabiliza la respuesta del filtro en un tiempo de 11.965 s en la onda theta. El estudio contó con una fs = 1000 Hz, cumpliendo con Nyquist. El orden del filtro no se menciona, pero sugiere que se obtuvo en artículos anteriores un menor error cuadrático medio (MSE) con Hanning de orden 120. La frecuencia de corte varió por onda EEG; en el caso de la theta, presentó una frecuencia de banda de paso de 4 Hz y una frecuencia de banda de rechazo de 8 Hz, acotada en sus rangos de identificación. Esto facilitó la eliminación del desplazamiento de la línea base provocado por el ojo y mejora la precisión en la detección de patrones críticos, como las crisis epilépticas [eeg6,eeg7].

#### Pasa bajos: 

Para la identificación de artefactos como el parpadéo y voluntarios como la masticación para mitigación y posible eliminación de señales EMG. Aplicar estos filtros, reduce drásticamente la amplitud y el contenido de frecuencia de la actividad de espigas de la Unidad simple motora (SMU), lo que hace que parezca una onda de EEG. Utilizar altas frecuencias de muestreo, mayor captación de datos pero mas costo computacional, y altos niveles de filtrado de paso bajo, al menos 1500 Hz [eeg3], para el registro y la evaluación de la señal de EEG, permite que la actividad de la SMU sea visible en los registros de EEG promediados por activación de espigas, de modo que se puedan crear algoritmos especiales para manejar estos artefactos. 

*Figura eeg1. Resultados representativos tras la aplicacion de una frecuencia de muestreo de 4096 Hz y los filtros se configuraron con un paso alto de 0.15 Hz y un paso bajo de 1500 Hz.[eeg3]*
<img width="600" height="400" alt="Captura de pantalla 2026-05-08 211512" src="https://github.com/user-attachments/assets/a3622c5d-844a-4dcc-870f-97ba94eaedd5" />


El estudio menciona que tras la obtención de la señal EEG limpia, se imtrodujeron señales que contenian ruidos por artefactos como parpadéos y masticación, para luego realizar los filtros paso altos y paso bajos, en ese respectivo orden, obteniendo la reconstrucción de la señal inicial.

### Generales:

#### Notch (Rechaza-banda)
Para la adquision de señales sEMG, ECG y EEG es común la presencia de interferencia de la red eléctrica,la cual introduce una componente sinusoidal 60 Hz, si hablamos del territorio peruano.
Para eliminar este tipo de ruido, se utiliza un filtro notch (rechaza-banda),diseñado para atenuar una banda muy estrecha de frecuencias centradas en 60 Hz. Este filtro permite suprimir la interferencia eléctrica sin afectar significativamente el resto del contenido de espectros de la señal biomédica.[1]
 
### Bibliografia 
[1] Polachan, K., Chatterjee, B., Weigand, S., & Sen, S. (2021). Human Body-Electrode Interfaces for Wide-Frequency Sensing and Communication: A Review. Nanomaterials (Basel, Switzerland), 11(8), 2152. https://doi.org/10.3390/nano11082152
[2] D. Pradon, L. Tong, C. Chalitsios, y N. Roche, “Development of surface EMG for gait analysis and rehabilitation of hemiparetic patients”, Sensors (Basel), vol. 24, núm. 18, p. 5954, 2024.
[eeg1]Mayo Clinic Staff, “Electroencefalografía (EEG),” Mayo Clinic, Sep. 18, 2024. [En línea]. Disponible en:https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875.[Accedido: 08-may-2026].
[eeg2] C. Novo-Olivas, L. Gutiérrez y J. Bribiesca, “Mapeo Electroencefalográfico y Neurofeedback,” en Aproximaciones al estudio de la neurociencia del comportamiento, M. A. Guevara Pérez, M. Arteaga Silva, A. Contreras Gómez y M. Hernández González, Eds. Guerrero, México: Universidad Autónoma de Guerrero, 2010, cap. XIII, pp. 371–412, ISBN: 978-970-764-911-8.
[eeg3]Yilmaz, G., Ungan, P., Sebik, O., Uginčius, P., & Türker, K. S. (2014). Interference of tonic muscle activity on the EEG: a single motor unit study. Frontiers in human neuroscience, 8, 504. https://doi.org/10.3389/fnhum.2014.00504
[eeg4] A. Pant y A. Kumar, "Exploración del procesamiento de señales EEG para el filtrado y la clasificación eficaces de crisis epilépticas," Discov. Electron., vol. 3, no. 20, 2026. [En línea]. Disponible en: https://doi.org/10.1007/s44291-026-00174-2
[eeg5] C. S. Nayak y A. C. Anilkumar, "EEG Normal Waves,"StatPearls. Treasure Island, FL, USA: StatPearls Publishing, 2026. [En línea]. Disponible en: https://www.ncbi.nlm.nih.gov/books/NBK539805/ 
[eeg6] A. Pant y A. Kumar, "Hanning FIR window filtering analysis for EEG signals," Biomedical Analysis, vol. 1, no. 2, pp. 111-123, Jun. 2024, doi: 10.1016/j.bioana.2024.05.003.
[eeg7] A. Pant, A. Kumar, C. Verma, y Z. Illés, "Comparative exploration on EEG signal filtering using window control methods," Results in Control and Optimization, vol. 17, art. 100485, dic. 2024, doi: 10.1016/j.rico.2024.100485.
