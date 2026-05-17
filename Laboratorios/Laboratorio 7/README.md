
<div align="center">

# Laboratorio 7:

<img width="850" height="300" alt="universidadperuanaCayetanoHeredia" src="https://github.com/user-attachments/assets/294153a6-16c6-40be-b47a-d5d1e62aee72" />

### Adquisición y análisis de señales electrocardiográficas (EEG) 

**Integrantes:** 
* Cárdenas Paniagua, Daniel Bagkdan 
* Soto Casasola, Maria Celina
* Zapata Castro, José Alonso
* Egusquiza Rubiños, Matias Enrique 
* Fuentes Hurtado, Astrid Nayeli 
 
**2026-I**

</div>

[Introducción](#Introducción)
[Metodología](#Metodología)

## Introducción:
La electroencefalografía (EEG) es un método no invasivo utilizado para registrar la actividad eléctrica cerebral mediante electrodos ubicados en el cuero cabelludo. Estas señales eléctricas provienen principalmente de los potenciales postsinápticos producidos por las neuronas piramidales de la corteza cerebral, cuya disposición paralela facilita la detección de las oscilaciones neuronales. A través del EEG es posible analizar distintas bandas de frecuencia cerebral, como delta, theta, alfa, beta y gamma. [1]
### Bandas de Frecuencia EEG:
<img width="800" height="400" alt="senialeseeg" src="https://github.com/user-attachments/assets/ab30c2d0-d431-4fd6-9af3-497f538fc33a" />

### Adquisición de la señal EEG:
La señal EEG puede obtenerse de forma monopolar, donde un electrodo activo es colocado respecto a una referencia común o bipolar, que mide la diferencia entre dos electrodos activos más una referencia. Por otro lado, una forma estandarizada de ubicar los electrodos en el cráneo humano es el sistema internacional 10-20, que distribuye las posiciones según porcentajes del tamaño del cráneo y usa letras para identificar las regiones corticales [2]:

| Código    |     Región   | Función |
|-----------|--------------|---------|
|F | Frontal | Funciones ejecutivas y atención|
|C |Central| Área motora|
|P |Parietal| Integración sensorial|
|O|Occipital|Procesamiento visual|
|T |Temporal| Audición, memoria y lenguaje|
|Z | Zero|Línea media|

<img width="600" height="400" alt="Captura de pantalla 2026-05-08 215208" src="https://github.com/user-attachments/assets/e52b698b-5a79-4805-b7a2-334f81da1255" />

## Metodología:


### Desarrollo en laboratorio - Evidencia: 

| Actividad                    | Ejecución | Señal obtenida (OpenSignals) |
|------------------------------|-----------|------------------------------|
| Reposo sin percepción visual |  <img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 9 59 41 PM" src="https://github.com/user-attachments/assets/56189c28-fb31-4f88-b16d-22b9f913155f" />|https://github.com/user-attachments/assets/020a761d-6678-46da-9c00-4fe0b34646fe|
| Mirando un punto fijo| <img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 10 00 19 PM" src="https://github.com/user-attachments/assets/b3cf403f-9d8b-4252-89f5-a59a4e1f2075" />| https://github.com/user-attachments/assets/99136424-bea0-469d-a342-1311f0b8089b |
|Segundo reposo sin percepción visual|<img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 10 01 02 PM" src="https://github.com/user-attachments/assets/8fc73bd7-4284-4f84-a044-d541beacf14e" />|https://github.com/user-attachments/assets/45c0d189-852b-4220-b3af-9e076dd9b365|
|Parpadeo y mastocación constante|<img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 10 01 55 PM" src="https://github.com/user-attachments/assets/89d82250-4750-4cd5-bd21-22607171030c" />|https://github.com/user-attachments/assets/c3098b89-0ea7-4088-9c85-729ed3c6bddb|
|Tercer reposo sin percepción visual|<img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 10 04 47 PM" src="https://github.com/user-attachments/assets/894d352c-01e1-42ac-8872-2ca0782c9276" />|https://github.com/user-attachments/assets/9bfc02d6-806f-4a3e-b623-595f2fd14040|
|Escuchando música relajante|<img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 10 05 31 PM" src="https://github.com/user-attachments/assets/dd55b88c-6758-4fd6-9dfa-5c371bc2ea33" />|https://github.com/user-attachments/assets/2e5355d6-d91a-437f-91c2-654536747154|
|Escuchando música estresante|<img width="1600" height="1200" alt="WhatsApp Image 2026-05-16 at 10 05 46 PM" src="https://github.com/user-attachments/assets/96e4a3fc-849d-4e32-99d6-4b868139c9ed" />|https://github.com/user-attachments/assets/cf62c87b-4638-4de0-b3a4-0ab5d6fe8304|

### Resultados:


<img width="1489" height="989" alt="1q" src="https://github.com/user-attachments/assets/bde94b3b-a19c-49e9-804a-d90cdd01c85a" />
<img width="1189" height="490" alt="1" src="https://github.com/user-attachments/assets/e66d95d3-e024-49b0-9cde-e729b3ca6869" />

*Figura 1. Gráficas de la señal temporal y espectral de una señal EEG en reposo, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*

<img width="1490" height="989" alt="2" src="https://github.com/user-attachments/assets/323ac983-5a22-46ac-adc7-89481c4034c4" />
<img width="1189" height="490" alt="descarga" src="https://github.com/user-attachments/assets/db2cb379-645b-44b5-b07f-7c3fa2f9e7dc" />

*Figura 2. Gráficas de la señal temporal y espectral de una señal EEG mirando a un punto fijo, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*

<img width="1490" height="989" alt="descarga (1)" src="https://github.com/user-attachments/assets/bf7f73fb-155b-44f8-851e-faae0fe6df9d" />
<img width="1189" height="490" alt="descarga (2)" src="https://github.com/user-attachments/assets/13808b68-909c-47d8-9db6-0dd24da3c569" />

*Figura 3. Gráficas de la señal temporal y espectral de una señal EEG en el segundo reposo tras la primera actividad, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*

<img width="1490" height="989" alt="descarga (3)" src="https://github.com/user-attachments/assets/893ad135-c0af-4699-8ff8-33170521b6e5" />
<img width="1189" height="490" alt="descarga (4)" src="https://github.com/user-attachments/assets/b8f8bf9e-d215-40d6-b85b-af7dedf12f7e" />

*Figura 4. Gráficas de la señal temporal y espectral de una señal EEG realizando parpadeos constantes y masticación simultáneamente, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*

<img width="1490" height="989" alt="descarga (5)" src="https://github.com/user-attachments/assets/b05f2a57-f630-4410-8c5e-8fd77b376438" />
<img width="1189" height="490" alt="descarga (6)" src="https://github.com/user-attachments/assets/9d202930-8e78-4e31-a3b4-7a12f6ea5876" />

*Figura 5. Gráficas de la señal temporal y espectral de una señal EEG tercera medición en reposo, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*

<img width="1490" height="989" alt="descarga (7)" src="https://github.com/user-attachments/assets/cd6129c1-e66e-4964-b649-4bf6ba96e2fc" />
<img width="1189" height="490" alt="descarga (8)" src="https://github.com/user-attachments/assets/383545be-c1af-4ff6-bcb6-696ad59c4bf5" />

*Figura 6. Gráficas de la señal temporal y espectral de una señal EEG resultados obtenidos mientras se escuchaba música considerada relajante por el sujeto de prueba, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*

<img width="1490" height="989" alt="descarga (9)" src="https://github.com/user-attachments/assets/2a568b91-8be8-4227-bbb2-01ff2adf3d31" />
<img width="1189" height="490" alt="descarga (10)" src="https://github.com/user-attachments/assets/ec3ca97b-d080-4264-87ce-4a2cdd49c872" />

*Figura 7. Gráficas de la señal temporal y espectral de una señal EEG resultados obtenidos mientras se escuchaba música estresante, antes y después del filtrado bandpass (1–40 Hz), mostrando la señal en el dominio del tiempo, su transformada rápida de Fourier (FFT), densidad espectral de potencia (PSD) y distribución de potencia en las bandas Delta, Theta, Alfa, Beta y Gamma*
### Discusion:
El análisis de la Densidad Espectral de Potencia (PSD) mediante el método de Welch se implementó para complementar y mejorar la información obtenida por la transformada rápida de Fourier (FFT). Mientras que la FFT original presenta fluctuaciones significativas debido al ruido  y la varianza en segmentos cortos de señales de electroencefalografía (EEG), el método de Welch mitiga este problema al dividir la señal temporal en ventanas solapadas. Al promediar los espectrogramas parciales de estas ventanas, se reduce drásticamente la varianza, proporcionando una estimación espectral mucho más estable y robusta para la cuantificación de la potencia en cada ritmo cerebral ($\delta, \theta, \alpha, \beta, \gamma$).[3]
### Efecto del Filtrado (1-40 Hz):
Al observar las gráficas comparativas, el filtrado pasabanda demuestra ser un paso crítico de preprocesamiento. En la señal original, la banda Delta presenta una potencia alta (superior a 600). Sin embargo, tras aplicar el filtro pasabanda de 1-40 Hz, esta potencia se reduce aproximadamente a la mitad. Esto sugiere que gran parte de la energía inicial cuantificada en Delta no era de origen puramente neurológico, sino que estaba fuertemente contaminada por artefactos fisiológicos de baja frecuencia, tales como la deriva de la línea base (baseline wander), movimientos oculares o micromovimientos del paciente. El filtro atenúa exitosamente estas interferencias, revelando una distribución espectral más realista. Adicionalmente, el filtro elimina componentes por encima de 40 Hz, mitigando posibles ruidos de alta frecuencia o interferencias electromagnéticas.[4]
### Análisis del Estado de Reposo:
Los resultados del sujeto evaluado concuerdan con la literatura para un estado en reposo. En el espectro filtrado, si bien Delta mantiene una magnitud considerable (común en registros donde aún persisten leves movimientos de fondo), la banda Alfa se establece como el ritmo cortical dominante en comparación con las bandas de mayor frecuencia. La prominencia de la banda Alfa es el biomarcador clásico de un estado de relajación mental, que esta particularmente asociado a momentos con los ojos cerrados o con baja carga cognitiva.
Por otro lado, la potencia de las bandas asociadas a la actividad cognitiva intensa, la concentración y el procesamiento de información (Beta y Gamma) se mantienen en niveles bajos. La banda Gamma es casi nula tras el filtrado, y Beta presenta una potencia  menor que Alfa y Theta. Esto indica que el protocolo de reposo fue exitoso y que el voluntario logró mantener un nivel adecuado de relajación mental y física sin tanta tensión o ansiedad.[5]
### Análisis del Estado - Mirando a un punto fijo:
Al analizar la densidad espectral de potencia (PSD) durante la tarea de fijación visual, se observa un cambio claro en la actividad cortical respecto al estado de reposo, asociado al aumento de atención y procesamiento visual.El cambio más evidente es la disminución de la banda Alfa, que pierde la predominancia observada en reposo. Esto corresponde al conocido “bloqueo alfa”, fenómeno que ocurre cuando el sujeto abre los ojos y dirige su atención a un estímulo visual. En contraste, la banda Beta aumenta considerablemente, lo cual es característico de estados de concentración y alerta. Mantener la mirada fija en un punto requiere una actividad cortical sostenida, especialmente en áreas relacionadas con la atención y el procesamiento visual.La banda Delta presenta una potencia elevada incluso después del filtrado. En un sujeto despierto, esto no suele deberse únicamente a actividad cerebral, sino también a artefactos biológicos. En este caso, los movimientos involuntarios de los ojos y los parpadeos probablemente contribuyen al aumento de energía en las frecuencias bajas, especialmente en las bandas Delta y Theta.[6]
### Referencias:
[1] Mayo Clinic. Electroencefalograma (EEG) [Internet]. Mayo Clinic; 2023 [citado 15 mayo 2026]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875
[2] Proença M, Mrotzeck K. BITalino Home Guide #3 – Electroencephalography (EEG). Lisbon: PLUX – Wireless Biosignals S.A.; 2021. Disponible en: https://bitalino.com
[3]	A. S. Al-Fahoum y A. A. Al-Fraihat, “Methods of EEG signal features extraction using linear analysis in frequency and time-frequency domains”, ISRN Neurosci., vol. 2014, p. 730218, 2014.
[4]	E. E. de Bitbrain, “Todo sobre los artefactos en EEG: detección y herramientas de filtrado”, Bitbrain, 08-ene-2026. [En línea]. Disponible en: https://www.bitbrain.com/es/blog/artefactos-eeg. [Consultado: 17-may-2026].
[5]	S. Getzmann, P. D. Gajewski, D. Schneider, y E. Wascher, “Resting-state EEG data before and after cognitive activity across the adult lifespan and a 5-year follow-up”, Sci. Data, vol. 11, núm. 1, p. 988, 2024.
[6]	A. Wróbel, “Beta activity: a carrier for visual attention”, Acta Neurobiol. Exp. (Wars.), vol. 60, núm. 2, pp. 247–260, 2000.




