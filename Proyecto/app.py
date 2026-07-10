import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt, iirnotch, welch

st.set_page_config(page_title='NeuroRead', page_icon='🧠', layout='wide')

st.markdown('''
<style>
[data-testid="stSidebar"] {background: linear-gradient(180deg, #111827, #1f2937);}
[data-testid="stSidebar"] * {color: white;}
[data-testid="stSidebar"] h1 {font-size: 34px;}
div[role="radiogroup"] label {
    background-color: rgba(255,255,255,0.08); padding: 12px; border-radius: 12px;
    margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.12);
    width: 205px; height: 52px; display: flex; align-items: center;
}
div[role="radiogroup"] label:hover {background-color: rgba(255,255,255,0.22);}
.card, .member-card, .analysis-card, .result-card {
    background-color: white; padding: 24px; border-radius: 20px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08); margin-bottom: 22px;
}
.analysis-card {background: linear-gradient(135deg, #ffffff, #f5fbf9); border: 1px solid #dbeee8;}
.result-card {text-align: center; border: 1px solid #e2e8f0;}
.block-container {padding-top: 2rem;}
.small-text {color: #475569; font-size: 15px;}
.metric-label {color: #475569; font-size: 15px;}
.metric-value {color: #0f172a; font-size: 30px; font-weight: 800;}
.progress-wrap {position: relative; width: 100%; margin: 18px 0 8px 0;}
.progress-gradient {height: 18px; border-radius: 999px; background: linear-gradient(90deg,#ef4444 0%,#facc15 50%,#22c55e 100%);}
.progress-marker {position:absolute; top:-5px; width:28px; height:28px; border-radius:50%; background:white; border:4px solid #0f766e; box-shadow:0 2px 8px rgba(15,118,110,.35); transform:translateX(-50%);}
.progress-labels {display:flex; justify-content:space-between; color:#64748b; font-size:13px; margin-top:6px;}
</style>
''', unsafe_allow_html=True)


def mostrar_imagenes_por_usuario(tipo, titulo, descripcion):
    usuarios = ['ASTRID', 'DANIEL', 'JOSE']
    lecturas = ['L1', 'L2', 'R1', 'R2']
    st.markdown(f'<div class="card"><h1>{titulo}</h1><p>{descripcion}</p></div>', unsafe_allow_html=True)
    for usuario in usuarios:
        st.markdown(f'<div class="card"><h2>{usuario.capitalize()}</h2><p class="small-text">Resultados organizados en el orden L1, L2, R1 y R2.</p></div>', unsafe_allow_html=True)
        cols = st.columns(4)
        for i, lectura in enumerate(lecturas):
            nombre_archivo = f'{tipo}_{usuario}_{lectura}.PNG'
            with cols[i]:
                st.markdown(f'### {lectura}')
                if os.path.exists(nombre_archivo):
                    st.image(nombre_archivo, use_container_width=True)
                else:
                    st.warning(f'No se encontró: {nombre_archivo}')


def mostrar_codigos():
    codigos = [
        ('📂 Código 1 — Carga de la señal EEG','Leer el archivo .txt y visualizar la señal EEG en el dominio del tiempo.', '''import numpy as np
import matplotlib.pyplot as plt

eeg = np.loadtxt("Signal_Name.txt")
fs = 1000
t = np.arange(len(eeg)) / fs

plt.figure(figsize=(12,4))
plt.plot(t, eeg)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal EEG - Ambos Canales")
plt.grid()
plt.show()'''),
        ('📂 Código 2 — Visualización de todos los canales','Mostrar simultáneamente los canales EEG registrados.', '''min1 = 0
max1 = 100
plt.figure(figsize=(12,10))
for i in range(df.shape[0]):
    plt.subplot(8,1,i+1)
    plt.plot(t, df.iloc[i,:])
    plt.title("Canal " + str(i+1))
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.xlim(min1, max1)
plt.subplots_adjust(hspace=0.5)
plt.show()'''),
        ('📂 Código 3 — Selección de un canal EEG','Seleccionar un canal específico para analizarlo en el tiempo.', '''eeg = np.loadtxt("Daniel_respuestas1.txt")
fs = 1000
canal7 = eeg[:,6]
t = np.arange(len(canal7)) / fs
plt.figure(figsize=(14,4))
plt.plot(t, canal7)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Canal 7")
plt.grid(True)
plt.show()'''),
        ('📂 Código 4 — Espectro de frecuencia','Calcular y visualizar el espectro de frecuencia mediante FFT.', '''N = len(canal7)
fft_vals = np.fft.rfft(canal7)
freqs = np.fft.rfftfreq(N, 1/fs)
amplitud = np.abs(fft_vals) / N
plt.figure(figsize=(12,5))
plt.plot(freqs, amplitud)
plt.xlabel("Frecuencia (Hz)")
plt.xlim(-10,60)
plt.ylabel("Amplitud")
plt.title("Espectro de Frecuencia - Canal 7")
plt.grid(True)
plt.show()'''),
        ('📂 Código 5 — Eliminación de componente DC','Remover el offset de la señal EEG y centrarla alrededor de cero.', '''canal7 = canal7 - np.mean(canal7)
plt.figure(figsize=(14,4))
plt.plot(t, canal7)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Canal 7 sin componente DC")
plt.grid(True)
plt.show()'''),
        ('📂 Código 6 — Filtrado 4–40 Hz y Notch 60 Hz','Aplicar un filtro pasa banda Butterworth y un filtro Notch para ruido de red.', '''from scipy.signal import butter, filtfilt, iirnotch
low = 4
high = 40
b, a = butter(4, [low/(fs/2), high/(fs/2)], btype='band')
canal_filtrado = filtfilt(b, a, canal7)
f0 = 60
Q = 30
b_notch, a_notch = iirnotch(f0/(fs/2), Q)
canal_filtrado = filtfilt(b_notch, a_notch, canal_filtrado)'''),
        ('📂 Código 7 — Señal filtrada en el tiempo','Visualizar la señal EEG después del filtrado.', '''t = np.arange(len(canal_filtrado)) / fs
plt.figure(figsize=(14,4))
plt.plot(t, canal_filtrado)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud filtrada")
plt.title("Señal EEG filtrada en el tiempo - Canal 7")
plt.grid(True)
plt.show()'''),
        ('📂 Código 8 — PSD mediante Welch','Calcular y visualizar la densidad espectral de potencia.', '''from scipy.signal import welch
f, psd = welch(canal_filtrado, fs=fs, window='hann', nperseg=4*fs, noverlap=2*fs, scaling='density')
plt.figure(figsize=(12,5))
plt.semilogy(f, psd)
plt.xlim(0.5, 45)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD")
plt.title("Densidad espectral de potencia - Welch - Canal 7")
plt.grid(True)
plt.show()'''),
        ('📂 Código 9 — Potencia por bandas EEG','Calcular y graficar la potencia en bandas Delta, Theta, Alpha, Beta y Gamma baja.', '''bandas = {"Delta": (0.5, 4), "Theta": (4, 8), "Alpha": (8, 13), "Beta": (13, 30), "Gamma baja": (30, 45)}
potencias = {}
for nombre, (fmin, fmax) in bandas.items():
    idx = np.logical_and(f >= fmin, f < fmax)
    potencias[nombre] = np.trapezoid(psd[idx], f[idx])
plt.figure(figsize=(8,5))
plt.bar(potencias.keys(), potencias.values())
plt.ylabel("Potencia")
plt.title("Potencia por bandas EEG - Canal 7")
plt.grid(axis='y')
plt.show()''')
    ]
    st.markdown('<div class="card"><h1>💻 Códigos empleados</h1><p>En esta sección se presentan los códigos utilizados para el procesamiento de señales EEG.</p></div>', unsafe_allow_html=True)
    for titulo, objetivo, codigo in codigos:
        st.markdown('<div class="member-card">', unsafe_allow_html=True)
        st.markdown(f'### {titulo}')
        st.write(objetivo)
        st.code(codigo, language='python')
        st.markdown('</div>', unsafe_allow_html=True)


def cargar_txt(uploaded_file):
    uploaded_file.seek(0)
    try:
        datos = np.loadtxt(uploaded_file)
    except ValueError:
        uploaded_file.seek(0)
        try:
            datos = np.loadtxt(uploaded_file, delimiter=',')
        except ValueError as exc:
            raise ValueError('El archivo debe contener únicamente datos numéricos separados por espacios, tabulaciones o comas.') from exc
    datos = np.asarray(datos, dtype=float)
    if datos.ndim == 1:
        datos = datos.reshape(-1, 1)
    elif datos.ndim != 2:
        raise ValueError('El archivo debe contener una señal 1D o una tabla 2D.')
    if datos.shape[0] <= 16 and datos.shape[1] > datos.shape[0]:
        datos = datos.T
    if not np.all(np.isfinite(datos)):
        raise ValueError('El archivo contiene valores vacíos, infinitos o no numéricos.')
    return datos


def procesar_concentracion_beta(datos, fs, indice_canal, limite_bajo=20.0, limite_alto=60.0):
    canal = datos[:, indice_canal].astype(float)
    if len(canal) < 50:
        raise ValueError('La señal es demasiado corta para realizar el análisis.')
    canal_sin_dc = canal - np.mean(canal)
    nyquist = fs / 2.0
    if nyquist <= 40:
        raise ValueError('La frecuencia de muestreo debe ser mayor de 80 Hz.')
    b, a = butter(4, [4/nyquist, 40/nyquist], btype='band')
    canal_filtrado = filtfilt(b, a, canal_sin_dc)
    if nyquist > 60:
        b_notch, a_notch = iirnotch(60/nyquist, 30)
        canal_filtrado = filtfilt(b_notch, a_notch, canal_filtrado)
    nperseg = min(int(4*fs), len(canal_filtrado))
    nperseg = max(nperseg, 32)
    noverlap = min(int(2*fs), nperseg//2)
    f, psd = welch(canal_filtrado, fs=fs, window='hann', nperseg=nperseg, noverlap=noverlap, scaling='density')
    idx_beta = np.logical_and(f >= 13, f < 30)
    idx_total = np.logical_and(f >= 4, f <= 40)
    if np.count_nonzero(idx_beta) < 2 or np.count_nonzero(idx_total) < 2:
        raise ValueError('No existen suficientes puntos espectrales para calcular la banda Beta.')
    potencia_beta = float(np.trapezoid(psd[idx_beta], f[idx_beta]))
    potencia_total = float(np.trapezoid(psd[idx_total], f[idx_total]))
    if potencia_total <= 0:
        raise ValueError('No fue posible calcular una potencia espectral válida.')
    beta_relativa = float(np.clip(100.0 * potencia_beta / potencia_total, 0, 100))
    if beta_relativa < limite_bajo:
        nivel, descripcion, emoji = 'BAJA', 'La proporción de potencia Beta es baja dentro del rango de 4–40 Hz.', '😴'
    elif beta_relativa < limite_alto:
        nivel, descripcion, emoji = 'MODERADA', 'La proporción de potencia Beta se encuentra en un rango intermedio.', '🙂'
    else:
        nivel, descripcion, emoji = 'ALTA', 'La proporción de potencia Beta es elevada dentro del rango de 4–40 Hz.', '🎯'
    return dict(
        canal_original=canal,
        canal_sin_dc=canal_sin_dc,
        canal_filtrado=canal_filtrado,
        frecuencias=f,
        psd=psd,
        idx_beta=idx_beta,
        potencia_beta=potencia_beta,
        potencia_total=potencia_total,
        beta_relativa=beta_relativa,
        nivel=nivel,
        descripcion=descripcion,
        emoji=emoji
    )


def mostrar_barra_concentracion(porcentaje):
    posicion = float(np.clip(porcentaje, 1.5, 98.5))
    st.markdown(f'''<div class="progress-wrap"><div class="progress-gradient"></div>
    <div class="progress-marker" style="left:{posicion}%;"></div>
    <div class="progress-labels"><span>Baja</span><span>Moderada</span><span>Alta</span></div></div>''', unsafe_allow_html=True)


with st.sidebar:
    st.markdown('# 🧠 NeuroRead')
    st.markdown('Análisis de concentración mediante EEG')
    st.divider()
    pagina = st.radio('Menú', ['🏠 Inicio','ℹ️ Información','🧠 Señales EEG','📈 PSD','📊 Comparación','🧪 Analizar EEG','💻 Códigos','👥 Equipo'], label_visibility='collapsed')

if pagina == '🏠 Inicio':
    st.markdown('''
    <div class="card">
        <h1>🧠 NeuroRead</h1>
        <h3>Análisis del consumo de videos de formato corto en la dinámica de ondas beta durante tareas de lectura y respuesta</h3>
        <p>
        NeuroRead es una plataforma web interactiva desarrollada para integrar el registro,
        procesamiento y visualización de señales electroencefalográficas (EEG) obtenidas durante
        actividades de lectura y respuesta. Su propósito es contribuir al estudio de la relación
        entre el consumo frecuente de videos de corta duración en plataformas como TikTok,
        Instagram Reels y YouTube Shorts, y distintos procesos cognitivos vinculados con la
        concentración, la atención sostenida y la retención de información en adultos jóvenes.
        </p>
        <p>
        La plataforma permite cargar archivos EEG en formato TXT, seleccionar el canal de interés
        y ejecutar automáticamente el procesamiento de la señal. El sistema elimina la componente
        DC, aplica un filtro pasa banda de 4 a 40 Hz, calcula la densidad espectral de potencia
        mediante el método de Welch y analiza especialmente la banda Beta, comprendida entre
        13 y 30 Hz, por su relación con estados de vigilia, atención activa y esfuerzo cognitivo.
        </p>
    </div>

    <div class="card">
        <h2>🎯 Objetivo de la plataforma</h2>
        <p>
        Evaluar de manera exploratoria la relación entre la frecuencia de consumo de videos de
        corta duración y los perfiles neurofisiológicos asociados con la concentración, la atención
        sostenida y la retención de información a corto plazo en estudiantes universitarios,
        mediante el análisis de señales EEG registradas durante tareas de lectura y respuesta.
        </p>
    </div>

    <div class="card">
        <h2>🔬 ¿Qué permite hacer NeuroRead?</h2>
        <p>
        NeuroRead permite visualizar señales EEG en el dominio del tiempo, analizar su contenido
        frecuencial mediante la densidad espectral de potencia, comparar registros entre
        participantes y sesiones, y estimar un nivel de concentración a partir de la potencia
        relativa de la banda Beta. Asimismo, la plataforma organiza los resultados en gráficas
        comprensibles para facilitar tanto la interpretación automática como el análisis manual.
        </p>
    </div>

    <div class="card">
        <h2>📚 Contexto del estudio</h2>
        <p>
        El proyecto se desarrolla con estudiantes universitarios de Ingeniería Biomédica de entre
        20 y 26 años. Durante el protocolo experimental, los participantes realizan una lectura de
        alta dificultad mientras se registran señales EEG en los canales frontales Fp1 y Fp2.
        Posteriormente, responden preguntas de comprensión lectora, lo que permite relacionar los
        resultados neurofisiológicos con el desempeño cognitivo observado.
        </p>
    </div>

    <div class="card">
        <h2>⚠️ Alcance académico</h2>
        <p>
        La clasificación del nivel de concentración presentada por NeuroRead es de carácter
        académico y exploratorio. Los resultados dependen de la calidad de la señal adquirida y
        no sustituyen una evaluación clínica, neuropsicológica ni diagnóstica.
        </p>
    </div>
    ''', unsafe_allow_html=True)

elif pagina == 'ℹ️ Información':
    st.markdown('''
    <div class="card">
        <h1>ℹ️ Información del proyecto</h1>
        <p>
        NeuroRead surge ante la necesidad de contar con una herramienta integrada que permita
        estudiar, dentro de un mismo entorno, la relación entre el consumo de videos de formato
        corto, el desempeño conductual y la actividad cerebral. La plataforma combina el análisis
        de señales EEG con información obtenida mediante cuestionarios de consumo digital y
        pruebas de comprensión lectora, proporcionando una aproximación objetiva y complementaria
        al estudio de los procesos cognitivos.
        </p>
    </div>

    <div class="card">
        <h2>📌 Planteamiento del problema</h2>
        <p>
        A pesar del uso creciente de plataformas como TikTok, Instagram Reels y YouTube Shorts,
        todavía no existe consenso sobre la forma en que la exposición frecuente a contenidos
        breves puede influir en la atención sostenida, la concentración, el procesamiento
        cognitivo y la retención de información. Gran parte de los estudios disponibles se basa
        en cuestionarios de autorreporte, los cuales permiten conocer hábitos de consumo, pero no
        muestran de manera directa los cambios en la actividad cerebral.
        </p>
        <p>
        Por este motivo, el uso de señales electroencefalográficas constituye una alternativa
        complementaria para observar respuestas neurofisiológicas durante tareas cognitivas.
        NeuroRead integra ambos enfoques y facilita la comparación entre variables conductuales
        y espectrales.
        </p>
    </div>

    <div class="card">
        <h2>🎯 Objetivo general</h2>
        <p>
        Evaluar la relación entre la frecuencia de consumo de videos de corta duración y los
        perfiles neurofisiológicos de concentración, atención sostenida y retención de información
        a corto plazo en estudiantes universitarios, mediante el análisis de señales
        electroencefalográficas.
        </p>
    </div>

    <div class="card">
        <h2>📍 Alcance del proyecto</h2>
        <p>
        El estudio se enfoca en adultos jóvenes universitarios de entre 20 y 26 años pertenecientes
        a la carrera de Ingeniería Biomédica. Se analizan señales obtenidas en los canales frontales
        Fp1 y Fp2, zonas seleccionadas por su relación con procesos de atención, esfuerzo cognitivo
        y concentración. Los resultados se comparan entre participantes con distintos niveles de
        consumo de videos cortos y diferentes niveles de uso problemático de redes sociales.
        </p>
    </div>

    <div class="card">
        <h2>🧪 Metodología experimental</h2>
        <p>
        Para la adquisición de las señales se utilizó la placa BITalino NeuroBIT, dos sensores
        bipolares de electroencefalografía, electrodos desechables de gel, una computadora con la
        aplicación OpenSignals y un cronómetro. Los electrodos se colocaron en las posiciones Fp1
        y Fp2 del sistema internacional 10–20, junto con un electrodo de referencia ubicado en la
        apófisis mastoides para estabilizar la medición.
        </p>
        <p>
        Durante el registro, los participantes leyeron un texto de muy difícil legibilidad,
        seleccionado mediante el Índice de Legibilidad de Flesch-Szigriszt. El texto obtuvo un
        puntaje de -4.15 y estuvo compuesto por 585 palabras, 18 oraciones y 1676 sílabas. Al
        finalizar, se aplicó una prueba de comprensión lectora para complementar la interpretación
        de las señales EEG.
        </p>
    </div>

    <div class="card">
        <h2>⚙️ Procesamiento de señales</h2>
        <p>
        La plataforma procesa las señales EEG mediante una secuencia automatizada. Primero elimina
        la componente DC para centrar la señal alrededor de cero. Luego aplica un filtro Butterworth
        pasa banda de 4 a 40 Hz y, cuando corresponde, un filtro Notch de 60 Hz. Posteriormente,
        calcula la densidad espectral de potencia mediante el método de Welch y extrae la potencia
        correspondiente a la banda Beta, entre 13 y 30 Hz.
        </p>
        <p>
        La potencia Beta relativa se calcula respecto a la potencia total del rango de 4 a 40 Hz.
        A partir de este valor, la plataforma genera una clasificación exploratoria de concentración
        baja, moderada o alta, y la presenta junto con la señal filtrada, el espectro de frecuencia
        y la gráfica específica de la banda Beta.
        </p>
    </div>

    <div class="card">
        <h2>🧠 Importancia de las ondas Beta</h2>
        <p>
        Las ondas Beta se relacionan con estados de vigilia, atención activa, pensamiento
        consciente, memoria de trabajo y resolución de problemas. Dentro de este rango pueden
        distinguirse subbandas: la Beta baja se asocia con concentración tranquila y sostenida,
        la Beta media con mayor energía y rendimiento cognitivo, y la Beta alta con niveles
        elevados de activación fisiológica o estrés. Por ello, su análisis debe realizarse junto
        con el contexto experimental y no interpretarse de manera aislada.
        </p>
    </div>

    <div class="card">
        <h2>💻 Tecnologías empleadas</h2>
        <p>
        NeuroRead fue desarrollada en Python utilizando Streamlit como framework para la interfaz
        web. NumPy se emplea para el manejo numérico de las señales, SciPy para el diseño de filtros
        y el cálculo de la PSD, y Matplotlib para la generación de las gráficas. La plataforma está
        diseñada para ejecutarse localmente y puede adaptarse posteriormente para su despliegue en
        Streamlit Cloud.
        </p>
    </div>

    <div class="card">
        <h2>⚠️ Limitaciones</h2>
        <p>
        Los resultados no deben generalizarse a otras poblaciones, debido a que el estudio se
        restringe a estudiantes universitarios de Ingeniería Biomédica entre 20 y 26 años. Además,
        el análisis se limita a los canales frontales Fp1 y Fp2, por lo que no representa la
        actividad de todas las regiones cerebrales involucradas en la concentración y la memoria.
        </p>
        <p>
        La calidad de las señales también puede verse afectada por parpadeos, movimientos
        musculares, desplazamiento de electrodos, estrés, fatiga, calidad del sueño o consumo de
        estimulantes. En consecuencia, la clasificación generada por la plataforma debe
        interpretarse únicamente como una estimación académica y exploratoria.
        </p>
    </div>
    ''', unsafe_allow_html=True)

elif pagina == '🧠 Señales EEG':
    mostrar_imagenes_por_usuario('GT','🧠 Señales EEG en el tiempo','Visualización de las señales EEG filtradas en el dominio del tiempo.')
elif pagina == '📈 PSD':
    mostrar_imagenes_por_usuario('PSD','📈 Densidad Espectral de Potencia','Visualización de la PSD obtenida mediante Welch.')
elif pagina == '📊 Comparación':
    mostrar_imagenes_por_usuario('GB','📊 Potencia por bandas EEG','Comparación de la potencia en bandas EEG mediante gráficos de barras.')
elif pagina == '🧪 Analizar EEG':
    st.markdown('''<div class="card"><h1>🧪 Analizador de concentración EEG</h1><p>Cargue un archivo <b>.txt</b>, seleccione la frecuencia de muestreo y el canal. Al pulsar <b>Analizar</b>, la plataforma eliminará la componente DC, aplicará un filtro pasa banda de 4–40 Hz, calculará la PSD mediante Welch y evaluará únicamente la potencia relativa de la banda Beta (13–30 Hz).</p></div>''', unsafe_allow_html=True)
    col_carga, col_config = st.columns([1.25,1])
    with col_carga:
        st.markdown('<div class="analysis-card"><h3>1. Cargar señal EEG</h3><p class="small-text">El archivo puede contener una o varias columnas numéricas.</p></div>', unsafe_allow_html=True)
        archivo_txt = st.file_uploader('Arrastre y suelte el archivo aquí', type=['txt'])
    with col_config:
        st.markdown('<div class="analysis-card"><h3>2. Configurar análisis</h3><p class="small-text">Use la frecuencia de muestreo de la adquisición.</p></div>', unsafe_allow_html=True)
        fs_analisis = st.number_input('Frecuencia de muestreo (Hz)', min_value=81, max_value=10000, value=1000, step=1)
    datos_eeg = None
    canal_seleccionado = None
    if archivo_txt is not None:
        try:
            datos_eeg = cargar_txt(archivo_txt)
            numero_muestras, numero_canales = datos_eeg.shape
            st.success(f'Archivo cargado: {numero_muestras:,} muestras y {numero_canales} canal(es).')
            canal_seleccionado = st.selectbox('Canal a analizar', list(range(1,numero_canales+1)), index=min(6,numero_canales-1), format_func=lambda x:f'Canal {x}')
            duracion = numero_muestras / float(fs_analisis)
            m1,m2,m3 = st.columns(3)
            m1.metric('Muestras', f'{numero_muestras:,}')
            m2.metric('Canales', numero_canales)
            m3.metric('Duración estimada', f'{duracion:.2f} s')
        except Exception as exc:
            st.error(str(exc))
    analizar = st.button('🧠 Analizar señal', type='primary', use_container_width=True, disabled=datos_eeg is None)
    if analizar and datos_eeg is not None and canal_seleccionado is not None:
        try:
            with st.status('Procesando señal EEG...', expanded=True) as estado:
                st.write('✓ Seleccionando canal')
                st.write('✓ Eliminando componente DC')
                st.write('✓ Aplicando filtro pasa banda 4–40 Hz')
                st.write('✓ Calculando PSD mediante Welch')
                st.write('✓ Integrando potencia Beta entre 13 y 30 Hz')
                resultado = procesar_concentracion_beta(datos_eeg, float(fs_analisis), canal_seleccionado-1)
                estado.update(label='Análisis completado', state='complete', expanded=False)
            st.markdown('---')
            st.markdown('## Resultado del análisis')
            col_resultado, col_beta = st.columns([1,1.25])
            with col_resultado:
                porcentaje = resultado['beta_relativa']
                st.markdown(f'''<div class="result-card"><div style="font-size:54px;">{resultado['emoji']}</div><h2>CONCENTRACIÓN {resultado['nivel']}</h2><p>{resultado['descripcion']}</p><div class="metric-value">{porcentaje:.1f}%</div><div class="metric-label">Potencia Beta relativa</div></div>''', unsafe_allow_html=True)
                mostrar_barra_concentracion(porcentaje)
                st.caption('Clasificación exploratoria: baja de 0 a < 20 %, moderada de 20 a < 60 %, alta de 60 a 100 %.')
            with col_beta:
                f = resultado['frecuencias']
                psd = resultado['psd']
                idx_beta = resultado['idx_beta']

                fig, ax = plt.subplots(figsize=(9,5))
                ax.plot(f[idx_beta], psd[idx_beta])
                ax.fill_between(f[idx_beta], psd[idx_beta], alpha=.25)
                ax.set_xlim(13,30)
                ax.set_xlabel('Frecuencia (Hz)')
                ax.set_ylabel('PSD')
                ax.set_title(f'Banda Beta (13–30 Hz) — Canal {canal_seleccionado}')
                ax.grid(True)
                st.pyplot(fig, use_container_width=True)
                plt.close(fig)

                st.metric(
                    'Potencia absoluta Beta',
                    f"{resultado['potencia_beta']:.6g}"
                )

            st.markdown('---')
            st.markdown('## Señal EEG filtrada en el tiempo')

            tiempo = np.arange(len(resultado['canal_filtrado'])) / float(fs_analisis)

            fig_tiempo, ax_tiempo = plt.subplots(figsize=(13,4))
            ax_tiempo.plot(tiempo, resultado['canal_filtrado'])
            ax_tiempo.set_xlabel('Tiempo (s)')
            ax_tiempo.set_ylabel('Amplitud filtrada')
            ax_tiempo.set_title(
                f'Señal EEG filtrada en el tiempo — Canal {canal_seleccionado}'
            )
            ax_tiempo.grid(True)
            st.pyplot(fig_tiempo, use_container_width=True)
            plt.close(fig_tiempo)

            st.markdown('## Espectro de frecuencia de la señal filtrada')

            canal_filtrado = resultado['canal_filtrado']
            N = len(canal_filtrado)
            fft_vals = np.fft.rfft(canal_filtrado)
            freqs_fft = np.fft.rfftfreq(N, 1 / float(fs_analisis))
            amplitud_fft = np.abs(fft_vals) / N

            idx_fft = np.logical_and(freqs_fft >= 4, freqs_fft <= 40)

            fig_fft, ax_fft = plt.subplots(figsize=(13,4))
            ax_fft.plot(freqs_fft[idx_fft], amplitud_fft[idx_fft])
            ax_fft.set_xlim(4, 40)
            ax_fft.set_xlabel('Frecuencia (Hz)')
            ax_fft.set_ylabel('Amplitud')
            ax_fft.set_title(
                f'Espectro de frecuencia filtrado (4–40 Hz) — Canal {canal_seleccionado}'
            )
            ax_fft.grid(True)
            st.pyplot(fig_fft, use_container_width=True)
            plt.close(fig_fft)

            st.warning(
                'Resultado académico y exploratorio; no reemplaza una evaluación '
                'clínica ni diagnostica trastornos de atención.'
            )
        except Exception as exc:
            st.error(f'No se pudo completar el análisis: {exc}')
elif pagina == '💻 Códigos':
    mostrar_codigos()
elif pagina == '👥 Equipo':
    st.markdown('<div class="card"><h1>👥 Equipo de trabajo</h1><p>Integrantes responsables del desarrollo de la plataforma NeuroRead.</p></div>', unsafe_allow_html=True)
    integrantes = [
        {'foto':'DanielCardenas.jpeg','nombre':'Daniel Bagkdan Cárdenas Paniagua','rol':'DSP Developer Junior','correo':'daniel.cardenas.p@upch.pe'},
        {'foto':'JoseZapata.jpeg','nombre':'José Alonso Zapata Castro','rol':'Software Developer','correo':'jose.zapata.c@upch.pe'},
        {'foto':'MatiasRubinhios.jpeg','nombre':'Matías Enrique Rubiños Egusquiza','rol':'General Coordination','correo':'matias.rubinos@upch.pe'},
        {'foto':'MariaSoto.jpeg','nombre':'Maria Celina Soto Casasola','rol':'General Coordination','correo':'maria.soto.casasola@upch.pe'},
        {'foto':'AstridFuentes.jpeg','nombre':'Astrid Nayeli Fuentes Hurtado','rol':'General Coordination','correo':'astrid.fuentes@upch.pe'}]
    for integrante in integrantes:
        st.markdown('<div class="member-card">', unsafe_allow_html=True)
        col1,col2,col3,col4 = st.columns([1.3,1.6,1.4,2])
        with col1:
            if os.path.exists(integrante['foto']): st.image(integrante['foto'], width=180)
            else: st.warning(f"No se encontró: {integrante['foto']}")
        with col2:
            st.markdown('### Nombre'); st.write(integrante['nombre'])
        with col3:
            st.markdown('### Rol'); st.write(integrante['rol'])
        with col4:
            st.markdown('### Contacto'); st.markdown(f"[{integrante['correo']}](mailto:{integrante['correo']})")
        st.markdown('</div>', unsafe_allow_html=True)