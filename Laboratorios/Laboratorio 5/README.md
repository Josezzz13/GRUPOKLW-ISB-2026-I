<div align="center">

# Laboratorio 5: Adquisión de señales ECG mediante BITalino

<img width="850" height="300" alt="universidadperuanaCayetanoHeredia" src="https://github.com/user-attachments/assets/294153a6-16c6-40be-b47a-d5d1e62aee72" />

### Título

**Integrantes:** 
* Cárdenas Paniagua, Daniel Bagkdan 
* Soto Casasola, Maria Celina
* Zapata Castro, José Alonso
* Egusquiza Rubiños, Matias Enrique 
* Fuentes Hurtado, Astrid Nayeli 
 
**2026-I**

</div>

[Introducción](#Introducción)
## Introducción
La electrocardiografía (ECG) es una técnica no invasiva que registra la actividad eléctrica del corazón mediante electrodos colocados sobre la superficie corporal. Esta actividad es originado en el nodo sinoauricular y se propaga hacia el nodo auriculoventricular,el haz de His y el sistema de Purkinje,lo que permite la activación coordinada del miocardio ventricular.[1] En la señal ECG se reconocen los componentes característicos del ciclo cardíaco, principalmente la onda P, el complejo QRS y la onda T, asociados respectivamente con la despolarización auricular, la despolarización ventricular y la repolarización ventricular.[2] 
Para el electrocardiografía (ECG),la banda de frecuencias significativas se encuentra entre los 0.05 Hz y los 150 Hz.[3]
Para esta práctica se utilizó el sistema BITalino,junto a su sensor de ECG y unos sets de electrodos de superficies,para el registro de 3 derivaciones bipolares de Einthoven,las derivaciones I, II y III nos permiten observar la actividad eléctrica cardíaca desde diferentes orientaciones del plano frontal.[4]  
El experimento que realizamos se consideró el estado basal, hiperventilación, actividad física e hipoventilación con el fin de observar cómo cambian la morfología y la estabilidad de la señal ante distintas condiciones fisiológicas,debido a que durante el ejercicio la frecuencia cardíaca aumenta en respuesta a que necesita satisfacer una mayor demanda metabólica, por lo que esta condición resulta útil para evaluar la respuesta cardiovascular registrada por ECG [5]

[Metodología](#Metodología)
## Metodología





### Resultados:

#### I. Primera señal basal obtenida en reposo

<img width="1155" height="742" alt="E1Señalbasal_D1" src="https://github.com/user-attachments/assets/403a6a8d-7287-4676-9148-bd274d25f9dc" />

**Figura 1:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG obtenida en resposo (I Derivada).[Elaboración propia]

Se observa una frecuencia cardíaca promedio de 65.4 bpm, con un picos de 69 bpm a los 2.4 segundos y pico menor de aproximadamente 62 bpm manteniendose constante entre los 4.7 s y los 5.2 s. Presenta picos R definidos con amplitudes entre 0.1 a 0.2.


<img width="1152" height="738" alt="E1señalbasal_D2" src="https://github.com/user-attachments/assets/91122ab8-436f-4fc1-abac-5d4bcd1ad91e" />

**Figura 2:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG obtenida en resposo (II Derivada).[Elaboración propia]

Se observa una frecuencia cardíaca media de 72.6 bpm y una mayor demarcación de la curva QRS respecto al análisis previo, lo que mejora la identificación de picos R presentando una amplitud entre 0.5 a 0.6, y la curva producida por P-QRS-T.

<img width="1145" height="761" alt="E1señalbasal_D3" src="https://github.com/user-attachments/assets/d7adf25f-c579-4ed7-a034-ed6b41a56358" />

**Figura 3:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG obtenida en resposo (III Derivada).[Elaboración propia]

Se observa una frecuencia cardíaca media de 72.0 bpm, con variaciones moderadas a lo largo del tiempo. El latido promediado presenta una definición clara de las ondas P, QRS y T, aunque con menor amplitud del complejo QRS en comparación con el procesamiento anterior. Se sugiere que tercera etapa de procesamiento mantiene la estabilidad en la detección de picos R con amplitud menor a la de la segunda derivada pero mayor a la primera y una ligera reducción en las características de alta frecuencia de la señal. 

#### II. Señal ECG obtenida después de la primera hiperventilación

<img width="1151" height="742" alt="E1_hiper_D1_V1" src="https://github.com/user-attachments/assets/3df72e91-e94b-4c47-9c77-95c423eec70f" />

**Figura 4:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la primera hiperventilación  (I Derivada).[Elaboración propia]

Se observa un curva regular QRS bien definidos y detección marcada de los picos R. Las ondas P,Q,R,S y T son claramente identificables, sin alteraciones en la conducción intraventricular. La frecuencia cardíaca media es de 76.4 bpm con oscilaciones entre leves y moderadas, presenta picos de bpm mayores a 82 en aproximadamente 1s reduciendose notablemente con el tiempo, lo que nos da entender variabilidad entre sinusoides por respiración aumentada gracias a la hiperventilación.

<img width="1153" height="735" alt="E1_hiper_D2_V1" src="https://github.com/user-attachments/assets/983c3a32-c089-4360-aadb-c8d8b0da4d71" />

**Figura 5:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la primera hiperventilación  (II Derivada).[Elaboración propia]

Se observa, en comparación con la señal anterior, una menor dispersión en el promedio de los puntos característicos P, Q, S y T, lo que sugiere una mayor consistencia en la morfología del latido promedio. La frecuencia cardíaca se mantiene similar, con un valor medio de 76.4 bpm. Sin embargo, se presentan variaciones transitorias, alcanzando picos cercanos a 79 bpm en el primer segundo, menor que el anterior, y va descendiendo hasta aproximadamente 73 bpm alrededor de los 17 segundos, incrementandose nuevamente antes de llegar a los 20 segundos. Esto indicaría que, antes de estabilizarse tras la hiperventilación, la frecuencia cardíaca presenta oscilaciones marcadas.

<img width="1152" height="757" alt="E1_hiper_D3_V1" src="https://github.com/user-attachments/assets/deec09a0-3202-4ea3-9dbd-31deb4b91d4c" />

**Figura 6:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la primera hiperventilación  (III Derivada).[Elaboración propia]

Se observa una señal ECG con picos R claramente definidos y un ritmo sinusal estable. La frecuencia cardíaca presenta un promedio de 74.5 bpm, con variaciones leves en un rango aproximado de 72.5 a 76.8 bpm, evidenciando una menor variabilidad en comparación con la fase previa. Asimismo, la morfología del latido promedio muestra una menor dispersión en las ondas P, Q, S y T, indicando una mayor consistencia en la conducción eléctrica cardíaca. Se sugiere una fase de estabilización tras la hiperventilación, caracterizada por la recuperación del equilibrio del sistema nervioso autónomo y la disminución de la influencia simpática.

#### III. Señal ECG obtenida después de la segunda hiperventilación tras 2 minutos de descanso de la primera

<img width="1153" height="756" alt="E1_hiper_D1" src="https://github.com/user-attachments/assets/22ab3696-4e7e-40c8-8627-b145e376e6ff" />

**Figura 7:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la segunda hiperventilación  (I Derivada).[Elaboración propia]

<img width="1155" height="760" alt="E1_hiper_D2" src="https://github.com/user-attachments/assets/a9dee4a9-f388-4c33-951f-7e3938b97264" />

**Figura 8:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la segunda hiperventilación  (II Derivada).[Elaboración propia]

<img width="1157" height="733" alt="E1_hiper_D3" src="https://github.com/user-attachments/assets/bc51a9a3-1ec8-47c4-82fa-edbeb34b5d14" />

**Figura 9:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la segunda hiperventilación   (III Derivada).[Elaboración propia]

#### IV. Segunda señal basal obtenida en reposo

<img width="1155" height="740" alt="E1_señalbasal_D1_final" src="https://github.com/user-attachments/assets/567caca0-cd32-495b-b9d0-999f69808b40" />

**Figura 10:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG segundo reposo (I Derivada).[Elaboración propia]

<img width="1121" height="793" alt="E1_señalbasal_D2" src="https://github.com/user-attachments/assets/a3ff99bb-1485-49fe-8fa9-5c7870ff5d78" />

**Figura 11:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG segundo reposo (II Derivada).[Elaboración propia]

<img width="1148" height="796" alt="E1_señalbasal_D3" src="https://github.com/user-attachments/assets/7e7ca61a-02ca-4720-a353-c1d93d434352" />

**Figura 12:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG segundo reposo (III Derivada).[Elaboración propia]

#### V. Señal ECG obtenida tras realizar 4 minutos de Buppers

<img width="1160" height="735" alt="E2_D1" src="https://github.com/user-attachments/assets/66d5f436-880e-487b-9db8-3014b1c7520c" />

**Figura 13:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG tras 4 minutos de buppers (I Derivada).[Elaboración propia]

<img width="1152" height="722" alt="E2_D2" src="https://github.com/user-attachments/assets/deadc5ae-dbed-4314-99f3-64f6983198d6" />

**Figura 14:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG tras 4 minutos de buppers (II Derivada).[Elaboración propia]

<img width="1152" height="728" alt="E2_D3" src="https://github.com/user-attachments/assets/110d6c6d-837d-4c8d-8b06-bc0cb87e2f69" />

**Figura 15:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG tras 4 minutos de buppers (III Derivada).[Elaboración propia]

#### VI. Señal ECG obtenida tras la hipoventilación

<img width="1152" height="727" alt="E3_hipoventilación_D1" src="https://github.com/user-attachments/assets/a668329f-eb62-45d7-b8d0-d541c959c91c" />

**Figura 16:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG adquisión después de la hipoventilación (I Derivada).[Elaboración propia]

<img width="1152" height="742" alt="E3_hipoventilación_D2" src="https://github.com/user-attachments/assets/a826b95c-765c-4b79-b610-b9476802a49a" />

**Figura 17:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG adquisión después de la hipoventilación (III Derivada).[Elaboración propia]

## Discusión 

### Dominio del tiempo - Señal basal
- De la primera gráfica al considerar el intervalo de 20 segundos (10 - 30 segundos en el muestreo de nuestra señal) obtenemos un conteo de 23 beats aproximadamente. Al hacer una multiplicación simple para obtener los 60 segundos (1 minuto), tenemos una cantidad de 69 bpm. Cumpliendo el rango en reposo de 60-100 bpm.
## Discusión 

### Dominio del tiempo - Señal basal
- De la primera gráfica al considerar el intervalo de 20 segundos obtenemos un conteo de 23 beats aproximadamente. Al hacer una multiplicación simple para obtener los 60 segundos (1 minuto), tenemos una cantidad de 69 bpm. Cumpliendo el rango en reposo de 60-100 bpm. Esto se corrobora con la gráfica del promedio de latidos individuales donde es un valor de 65,4. Además, la frecuencia cardiáca presenta un valor mínimo de 62 hasta un valor máximo de 69 durante este tramo de tiempo.

- Realizando este mismo análisis para las derivadas 2 y 3, notamos que el rango de pulsaciones por minuto se encuentra en el rango de 60 a 100 bpm. Esto concuerda con la información literaria de Guyton y Hall, donde se especifica que el valor de bpm se situa alrededor de 72 para adultos  en reposo y que el intervalo siempre es situado entre 60 - 100 bpm. [a]
  
- A partir de la 4, 5 y 6ta figura nos encontramos en Hiperventilación. Analizando la primera derivada denotamos que los picos R que han aparecido son 26 durante los 20 segundos, lo que nos daría una frecuencia de 78 bpm. Realizando la comparación con las otras derivadas durante esta actividad de hiperventilación, notamos que todas presentan el mismmo incremento mínimo en el promedio de bpm, donde el valor mínimo es de 68 (en la segunda derivada) y el máximo es de 80 bpm en las gráficas de Heart Rate.

- Durante la segunda Hiperventilación (figuras 7, 8 y 9) observamos el mínimo patrón de aumento, sin embargo esto lleva a cuestionarnos porque ese aumento no es tan considerado como lo esperado en un estudio de hiperventilación inducida para adultos donde se menciona que el rango de este aumento se da entre 15 +/- 9 bpm para un rango de edad superior al de 55 años. [b] No obstante, el participante para la obtención de las señales es un deportista adulto joven de natación de 22 años, por lo que se espera su adaptamiento con un control adecuado de respiraciones por lo que este resultado no variara considerablemente como el presentado en el estudio.
  
- Realizando la segunda medición del reposo se obtuvieron los siguientes valores para el conteo de picos R en la primera gráfica de cada derivada: 23x3, 24x3 y 24x3. Esto nos da un conteo de 69, 72 y 72 bpm para la primera, segunda y tercera derivada respectivamente. Estos resultados tienen sentido, ya que tras haber realizado la hiperventilación y encontrarse en reposo, se espera la obtención de un valor en los intervalos de 64 - 80 bpm, siendo ambos números el mínimo valor obtenido durante el primer reposo y el máximo valor obtenido durante la hiperventilación (figuras 10,11 y 12)

- Desde la figura 13 hasta la 15 comenzamos el análsis para actividad física. En la primera gráfica de D-I obtenemos un conteo de 46 x 3 = 138 picos R, esto nos indica que los bpm se encuentran alrededor de ese valor. Corroboramos la información calculada por la gráfica de Individual Heart Beats donde el promedio es de 138.9 bpm y este mismo procedimiento se verifica para la gráfica de Heart Rate, donde el rango de valores es de 136 a 143 bpm durante los 20 segundos. Realizamos el mismo procedimiento para las Derivadas II y III y observamos el mismo patrón, donde cada una tiene un promedio de 121 y 115 bpm. Este resultado concuerda con el concepto del libro Guyton y Hall que afirma que durante una actividad física la frecuencia cardiaca esperada debe encontrarse en valores superiores a 100 bpm. [a]

- En general, durante la actividad física el electrocardiograma evidencia un incremento claro en la frecuencia de los latidos cardiacos. Este comportamiento refleja una respuesta fisiológica normal mediada por la activación del sistema nervioso simpático, la cual induce un aumento de la frecuencia cardiaca para cubrir las mayores demandas metabólicas del organismo. [d]

- MARIA 1
- MARIA 2

- La experiencia de laboratorio fue eficaz, se obtuvieron valores concordantes con literaturas fisiológicas e investigaciones científicas respecto al tema. Sin embargo, se presentaron ciertas limitaciones durante el desarrollo de las mediciones.
  - La primera dificultad fue la conectividad del sensor bitalino con el software en la laptop para la tranmsisión de la data. Esto retrasaba la medición y a su vez, recaía en la pérdida de data como es observable en el caso de actividad física para la segunda derivada. Al tardar en realizar la conexión, el sujeto de prueba durante la espera estaba sometido al reposo, regularizando su frecuencia cardiaca y ocasionando la pérdida de esa data. Para compensarlo, fue sometido a otros 2 minutos extra de burpees y poder obtener la data para la 3ra derivada.
  - La segunda limitación es la demora de colocación de sensores al cambio de derivadas, no es notable pero los primeros picos R no son identificados como sería el caso de la gráfica 9, ocasionando una pérdida de data no detectable a simple vista.
  -  Agreguen alguna otra limitación uwu

## Referencias
- [1]Y. Sattar y L. Chhabra, “Electrocardiogram”, en StatPearls, Treasure Island (FL): StatPearls Publishing, 2026.
- [2] E. A. Ashley y J. Niebauer, Conquering the ECG. Londres, Inglaterra: REMEDICA
- [3]L. G. Tereshchenko y M. E. Josephson, “Frequency content and characteristics of ventricular conduction”, J. Electrocardiol., vol. 48, núm. 6, pp. 933–937, 2015
- [4]EXPERIMENTAL GUIDES TO MEET y L. Y. Biosignals, “BITalino (r)evolution Lab Guide”, Pluxbiosignals.com. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf.
- [5]A. Akulwar, “Comparing heart rate recovery after aerobic vs. Anaerobic exercise”, Int. J. Med. Biomed. Stud., vol. 2, núm. 3, 2018

- [a] Hall, J. E. (2021). Guyton and Hall Textbook of Medical Physiology (14th ed.). Elsevier

- [b] Hawkins SM, Guensch DP, Friedrich MG, Vinco G, Nadeshalingham G, White M, Mongeon FP, Hillier E, Teixeira T, Flewitt JA, Eberle B, Fischer K. Hyperventilation-induced heart rate response as a potential marker for cardiovascular disease. Sci Rep. 2019 Nov 29;9(1):17887. doi: 10.1038/s41598-019-54375-9. PMID: 31784617; PMCID: PMC6884614.

- [c] imagen xd --> https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

- [d] J. Naranjo-Orellana et al., "Cardiovascular response to exercise: Integrative physiology insights," Frontiers in Physiology, vol. 12, p. 667116, 2021, doi: 10.3389/fphys.2021.667116.
