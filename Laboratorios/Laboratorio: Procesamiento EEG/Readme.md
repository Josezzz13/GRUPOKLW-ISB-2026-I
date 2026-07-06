<div align="center">

# Laboratorio 8

<img width="850" height="300" alt="universidadperuanaCayetanoHeredia" src="https://github.com/user-attachments/assets/294153a6-16c6-40be-b47a-d5d1e62aee72" />

### Aplicación de ICA en señales EEG

**Integrantes:** 
* Cárdenas Paniagua, Daniel Bagkdan 
* Soto Casasola, Maria Celina
* Zapata Castro, José Alonso
* Rubiños Egusquiza, Matias Enrique 
 * Fuentes Hurtado, Astrid Nayeli
   
**2026-I**

</div>

## Metodología
Para la adquisición y el procesamiento de señales electroencefalográficas, se emplearon los siguientes materiales:
- Placa del sistema BITalino NeuroBIT
- 2 sensores bipolares de electroencefalografía
- Electrodos desechables de gel.
- Computadora portátil con la aplicación Open Signals instalada.
- Cronómetro de un dispositivo móvil.
Primero, se realizó la identificación de los puntos anatómicos adecuados para obtener las señales de interés dentro de las limitaciones de medición (no se puede hacer mediciones en el cuero cabelludo debido al cabello). En este caso, se trabajó con canales Fp1 y Fp2 ubicados en la región frontal correspondientes al sistema internacional 10–20 de colocación de electrodos para la medición de EEG que pueden observarse en la Figura 1. 
<p align="center">
  <img width="850" height="468" alt="Image" src="https://github.com/user-attachments/assets/19727f2e-310c-49e5-aa37-01775dff6bb3" />
</p>
<p align="center">
  <b>Figura 1:</b> Sistema internacional 10-20 de distribución anatómica de canales de EEG [1]
</p>


Adicionalmente, se colocó un electrodo de referencia en la apófisis mastoides, con el objetivo de estabilizar la medición, siguiendo las indicaciones de la guía de laboratorio de BITalino para EEG, como se muestra en la Figura 2.
<p align="center">
  <img src="https://github.com/user-attachments/assets/fad30d66-6f85-464e-8473-661a3856c53d" height="400"/>
</p>
<p align="center">
  <b>Figura 2:</b> Ubicación de electrodos bipolares y el de referencia para lectura de canales EEG Fp1 y Fp [2]
</p>

Luego, se escoge una lectura de muy difícil legibilidad de acuerdo al Índice de Legibilidad de Flesch-Szigriszt determinado por la siguiente ecuación:

<img width="587" height="74" alt="Image" src="https://github.com/user-attachments/assets/713960c5-7e42-43db-98a8-f28cfaa0c9c6"/>

donde S, P y F son la cantidad de sílabas, palabras y frases/oraciones del texto correspondientemente.
Además, se consideró que la temática del texto estuviera fuera del dominio académico de los participantes de este proyecto de investigación. En este caso, se trata de un texto sobre política interior de Palestina que se presenta a continuación:

“Política interior de Palestina:
Tras la muerte en 2004 del presidente de la Autoridad Palestina, Yasser Arafat, se celebraron elecciones presidenciales el 9 de enero de 2005, siendo elegido nuevo presidente Mahmoud Abbas «Abu Mazen» con un 63 % de los votos. En las elecciones legislativas palestinas celebradas en enero de 2006 se produjo un vuelco electoral al ganar Hamas 76 escaños de los 132 con los que contaba la Asamblea Legislativa palestina. Fatah logró 43 diputados. El gabinete Qurei presentó su dimisión y Abbas reconoció la victoria de Hamas.
La división entre los principales partidos, Fatah y Hamas, junto a los disturbios desatados en Palestina, especialmente en la Franja de Gaza, provocaron enfrentamientos armados durante la primavera de 2007, que desembocaron en la toma del poder por parte de Hamas en Gaza en junio de ese año, estableciéndose desde entonces una división entre Cisjordania y la Franja de Gaza (donde el Gobierno de facto ha estado en manos de Hamas hasta la guerra en Gaza que comenzó tras los atentados terroristas del 7 de octubre de 2023). 
Desde 2006 no ha habido elecciones legislativas ni presidenciales en Palestina, por lo que sigue pendiente la renovación tanto de la Jefatura del Estado como del Consejo Legislativo Palestino, suspendido en 2017 por el Presidente Abbas. En octubre de 2012 tuvieron lugar solamente elecciones municipales en Cisjordania. 
El 15 de enero de 2021 Mahmoud Abbas aprobó el decreto por el cual se convocaban elecciones legislativas para el 22 de mayo y presidenciales para el 31 de julio. Si bien no era la primera vez que se había expresado la intención de llevarlas a cabo, la firma del decreto sí anunciaba un cambio en esta ocasión. Con todo, al incluir como condición necesaria la participación de Jerusalén Este, el proceso quedaba en manos del gobierno israelí, quien en ningún momento se manifestó al respecto, a pesar de la presión por parte de la comunidad internacional. Este fue el argumento esgrimido por el Presidente para posponer las elecciones, alegando que no se retomarían hasta asegurar el permiso por parte de Israel. 
Frente a las críticas por la falta de una nueva convocatoria a nivel nacional, el 12 de diciembre se celebraron elecciones locales en 154 localidades de Cisjordania, en las que participó un 66,14% de la población y cuya victoria recaló, por amplio margen, en las listas independientes frente a los partidos tradicionales, que recibieron menos del 30% de los votos. La segunda fase se llevó a cabo el 26 de marzo de 2022. Hamás apostó por no participar en el proceso hasta la celebración de las elecciones nacionales. 
El ataque terrorista de Hamas del pasado 7 de octubre de 2023 y la subsiguiente guerra en Gaza han cambiado radicalmente los parámetros de la vida política palestina. Existe un consenso internacional para que la Autoridad Palestina vuelva a asumir el gobierno de la Franja de Gaza, algo a lo que se opone Israel. En todo caso, para la AP es necesario que haya un cese completo en las hostilidades como condición previa a su entrada en la Franja y la comunidad internacional, especialmente los Estados Unidos, reclama todo un proceso previo de reforma interna y la conformación de un nuevo Gobierno de corte tecnocrático. El 15 de marzo de 2024, el Presidente Abbas designó a Muhamad Mustafa como nuevo Primer Ministro (PM) y le encargó la conformación de un nuevo Gobierno de corte reformista. El nuevo Ejecutivo fue oficialmente designado el 28 de marzo y tomó posesión el 31 de marzo de 2024.”

En el texto anterior se obtienen 585 palabras, 18 oraciones y 1676 sílabas, lo que le da un puntaje de -4,15 y lo establece como un texto de muy difícil legibilidad (<40), esto con el objetivo de exigir toda la atención posible por parte del participante.
A partir de la medición de un participante durante la lectura del texto establecido, se realizó:
- el ploteo de la señal en el dominio temporal
- el preprocesamiento básico con la aplicación de un filtro pasa banda (0.5–40 Hz) y un filtro notch (50/60 Hz).
- implementación de ICA con la librería MNE-Python
- ploteo de componentes relacionadas con artefactos (parpadeo, movimiento ocular o ruido muscular).
- reconstrucción de la señal EEG eliminando dichas componentes y
- comparación la señal original y la señal corregida.

## Resultados
### 1) Configuracion de Datos y Filtrado
- Estructura del objeto MNE: Se cargo la señal en un objeto con una frecuencia de muestreo de 100 Hz registrado 80001 puntos de tiempo (duracion de 01:21 min) que fueron mapeados sobre 64 canales.
- Filtro de Paso Alto: Se aplico un filtro FIR de fase cero con ventana de Hamming con un limite de 1 Hz con un frecuencia de corte de -6dB en 0.5 Hz para eliminar derivas del baseline y estabilizar la señal.

## 2) Descomposicion por ICA
- Ajuste del Algoritmo: Se utilizo el metodo de optimizacion Picard restringido a un maximo de 500 iteraciones.
- Convergencia: El algoritmo convergio de forma rapido en 91 iteraciones, reduciendo la varianza a partir de 64 componentes de PCA para extraer 2 componentes independientes (ICA) principales.

## 3) Identificacion Visual y Espacial de Artefactos
- Analisis Temporal: Mientras que la componente ICA000 se mantuvo relativamente homogenea, la componente ICA001 muestra deflexiones transitorias destacando un pico de ruido a los 12.5 segundos.
- Localizacion Espacial: La componente ICA000 se concentro en la zona frontal izquierda mientras que ICA001 exhibio una fuerte polarizacion en la region frontal anterior derecha que coincide justamente con el electrodo Fp2.
- Diagnostico de ICA001: Al evaluar 40 segmentos temporales, la componente arrrojo
ciertos picos de varianza (segmentos 6 y 19) y una caida espectral de artefactos musculares u oculares.

## 4) Seleccion y Exclusion de Componentes
- Criterio Automatico: Con una ventana de 2.048 segundos la deteccion automatizada no arrojo marcas criticas de ruido muscular de forma independiente.
- Criterio Manual: En los mapas topograficos y señales la componente ICA001 correspondia a un artefacto muscular frontal derecho, se marco manualmente para su exclusion registrando un score de 0.00078.

## 5) Reconstruccion y Señal EEG Limpia
Tras aplicar la proyeccion inversa para eliminar la componente ICA001, se evaluaron los 3 primeros segundos de la señal reconstruida:
- Datos EEG Crudos: La señal original presentaba un artefacto muscular masivo en el segundo 0.5 que caia drasticamente hasta los -200 unidades arbitrarias, mientras que en la señal corregida este artefacto fue completamente suprimido
- Potencial de Campo Global: El pico de energia artifical es de 30 unidades provocado por el ruido en el segundo 0.5 disminuyo sustancialmente en la señal corregida regresando a valores basales.
- Promedio de Canales: El trazo promedio se mantuvo igual tanto antes y despues de la limpieza, esto demuestra que el algoritmo ICA elimino con exito el ruido del electrodo prefrontal derecho sin alterar ni perder informacion general del resto del registro.

## Conclusiones

## Bibliografía
[1] ResearchGate, "Figura 3. Sistema Internacional 10-20 para la colocación de los electrodos," Imagen, [En línea]. Disponible en: https://www.researchgate.net/figure/Figura-3-Sistema-Internacional-10-20-para-la-colocacion-de-los-electrodos_fig2_282294960

[2] PLUX Biosignals, “HomeGuide3 EEG,” Manual técnico, 2022. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf.

