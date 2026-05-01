<div align="center">

# Laboratorio 5: Adquisión de señales ECG mediante BITalino

<img width="850" height="300" alt="universidadperuanaCayetanoHeredia" src="https://github.com/user-attachments/assets/294153a6-16c6-40be-b47a-d5d1e62aee72" />

### Título

**Integrantes:** 


 Fuentes Hurtado, Astrid Nayeli
 
**2026-I**

</div>

[Introducción](#Introducción)
## Introducción

[Metodología](#Metodología)
## Metodología

### Resultados:
<img width="1155" height="742" alt="E1Señalbasal_D1" src="https://github.com/user-attachments/assets/403a6a8d-7287-4676-9148-bd274d25f9dc" />

**Figura 1:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG obtenida en resposo (I Derivada).[Elaboración propia]

Se obtuvo una frecuencia cardíaca media de 65.4 bpm con morfología consistente de ondas P-QRS-T y baja variabilidad entre latidos. 

<img width="1152" height="738" alt="E1señalbasal_D2" src="https://github.com/user-attachments/assets/91122ab8-436f-4fc1-abac-5d4bcd1ad91e" />

**Figura 2:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG obtenida en resposo (II Derivada).[Elaboración propia]

Se observa una frecuencia cardíaca media de 72.6 bpm y una mayor prominencia del complejo QRS respecto al análisis previo, lo que mejora la identificación de picos R y la delineación de la morfología P-QRS-T.

<img width="1145" height="761" alt="E1señalbasal_D3" src="https://github.com/user-attachments/assets/d7adf25f-c579-4ed7-a034-ed6b41a56358" />

**Figura 3:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG obtenida en resposo (III Derivada).[Elaboración propia]

Se observa una frecuencia cardíaca media de 72.0 bpm, con variaciones moderadas a lo largo del tiempo. El latido promedio presenta una definición clara de las ondas P, QRS y T, aunque con menor amplitud del complejo QRS en comparación con el procesamiento anterior. Este resultado sugiere que la tercera etapa de procesamiento mantiene la estabilidad en la detección de picos R, pero con una ligera reducción en las características de alta frecuencia de la señal. 

<img width="1153" height="756" alt="E1_hiper_D1" src="https://github.com/user-attachments/assets/22ab3696-4e7e-40c8-8627-b145e376e6ff" />

**Figura 4:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la hiperventilación  (I Derivada).[Elaboración propia]

<img width="1155" height="760" alt="E1_hiper_D2" src="https://github.com/user-attachments/assets/a9dee4a9-f388-4c33-951f-7e3938b97264" />

**Figura 5:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la hiperventilación  (II Derivada).[Elaboración propia]

<img width="1157" height="733" alt="E1_hiper_D3" src="https://github.com/user-attachments/assets/bc51a9a3-1ec8-47c4-82fa-edbeb34b5d14" />

**Figura 6:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG después de la hiperventilación   (III Derivada).[Elaboración propia]

<img width="1155" height="740" alt="E1_señalbasal_D1_final" src="https://github.com/user-attachments/assets/567caca0-cd32-495b-b9d0-999f69808b40" />

**Figura 7:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG segundo reposo (I Derivada).[Elaboración propia]

<img width="1121" height="793" alt="E1_señalbasal_D2" src="https://github.com/user-attachments/assets/a3ff99bb-1485-49fe-8fa9-5c7870ff5d78" />

**Figura 8:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG segundo reposo (II Derivada).[Elaboración propia]

<img width="1148" height="796" alt="E1_señalbasal_D3" src="https://github.com/user-attachments/assets/7e7ca61a-02ca-4720-a353-c1d93d434352" />

**Figura 9:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG segundo reposo (III Derivada).[Elaboración propia]

<img width="1160" height="735" alt="E2_D1" src="https://github.com/user-attachments/assets/66d5f436-880e-487b-9db8-3014b1c7520c" />

**Figura 10:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG tras 4 minutos de buppers (I Derivada).[Elaboración propia]

<img width="1152" height="722" alt="E2_D2" src="https://github.com/user-attachments/assets/deadc5ae-dbed-4314-99f3-64f6983198d6" />

**Figura 11:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG tras 4 minutos de buppers (II Derivada).[Elaboración propia]

<img width="1152" height="728" alt="E2_D3" src="https://github.com/user-attachments/assets/110d6c6d-837d-4c8d-8b06-bc0cb87e2f69" />

**Figura 12:** Procesamiento de señal ECG con detección de picos R, cálculo de frecuencia cardíaca y promedio de latidos - ECG tras 4 minutos de buppers (III Derivada).[Elaboración propia]

## Discusión 

### Dominio del tiempo - Señal basal
- De la primera gráfica al considerar el intervalo de 20 segundos (10 - 30 segundos en el muestreo de nuestra señal) obtenemos un conteo de 23 beats aproximadamente. Al hacer una multiplicación simple para obtener los 60 segundos (1 minuto), tenemos una cantidad de 69 bpm. Cumpliendo el rango en reposo de 60-100 bpm.


## Referencias
