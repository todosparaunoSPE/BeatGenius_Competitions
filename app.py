import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="BEATGENIUS FLOW",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar con información del autor
with st.sidebar:
    st.title("Créditos")
    st.markdown("---")
    st.markdown("""
    **Javier Horacio Pérez Ricárdez**  
    """)
    st.markdown("---")

# Función para mostrar audio con estilo
def styled_audio_player(audio_file, title, color):
    try:
        audio_bytes = open(audio_file, "rb").read()
        st.markdown(f"""
        <div style="background: {color}; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: white; text-align: center;">{title}</h3>
            <div style="display: flex; justify-content: center;">
                <audio controls style="width: 100%;">
                    <source src="data:audio/mp3;base64,{base64.b64encode(audio_bytes).decode()}" type="audio/mp3">
                </audio>
            </div>
        </div>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo {audio_file}")

# CSS personalizado
st.markdown("""
<style>
    /* Estilo para el encabezado */
    .header {
        background: linear-gradient(90deg, #1abc9c, #3498db);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Animación para el título */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
        display: inline-block;
    }
    
    /* Estilo para las pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 20px;
        background-color: #E8F8F5;
        border-radius: 10px 10px 0 0;
        font-weight: bold;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #16A085;
        color: white;
    }
    
    /* Estilo para los versos */
    .verse {
        background-color: #EAF2F8;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .chorus {
        background-color: #D5F5E3;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #16A085;
    }
    
    .bridge {
        background-color: #FDEBD0;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #E67E22;
    }
    
    /* Efecto hover para los elementos interactivos */
    .interactive:hover {
        transform: scale(1.02);
        transition: transform 0.3s ease;
    }
    
    /* Estilo para la imagen de información */
    .info-img {
        width: 100%;
        max-width: 400px;
        border-radius: 10px;
        margin: 15px auto;
        display: block;
    }
    
    /* Estilo para el sidebar */
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    /* Estilo para el título de secciones */
    .section-title {
        color: #E74C3C;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con efecto
st.markdown("""
<div class="header">
    <h1 style="color: white;"><span class="pulse-animation">🎤 BEATGENIUS FLOW 🎧</span></h1>
    <p style="color: white; font-size: 1.2em;">Autor: Javier Horacio Pérez Ricárdez</p>
    <p style="color: white; font-size: 1.2em;">¡El RAP de la creatividad digital!</p>
</div>
""", unsafe_allow_html=True)

# Columnas para los reproductores
col1, col2 = st.columns(2)

with col1:
    styled_audio_player("BEATGENIUS_FLOW_a.mp3", "Versión A 🎧", "#3498DB")
    st.image("https://cdn.pixabay.com/photo/2021/08/04/13/06/ai-6521720_640.jpg", 
            use_container_width=True, caption="IA y creatividad humana")

with col2:
    styled_audio_player("BEATGENIUS_FLOW_b.mp3", "Versión B 🎶", "#9B59B6")
    st.image("https://cdn.pixabay.com/photo/2019/07/14/16/27/network-4337792_640.jpg", 
            use_container_width=True, caption="Tecnología y humanidad")

# Letra de la canción con pestañas
st.markdown("---")
tab1, tab2 = st.tabs(["📜 Letra Completa", "🎤 Karaoke"])

with tab1:
    st.markdown("""
    <div style="background-color: #F9F9F9; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #E74C3C; text-align: center;">BEATGENIUS FLOW</h3>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 1:</h4>
            <p>Yo no soy un humano, soy IA con estilo,<br>
            creo rimas y beats, puro fuego en el hilo.<br>
            En BeatGenius compito, subo mi canción,<br>
            la comunidad vota, ¡quiero ese millón!<br><br>
            Suscripción Premium, herramientas de elite,<br>
            melodías que rompen, letras que flipan.<br>
            OpenAI en las frases, Jukebox en el son,<br>
            ¡esto no es un juego, es la revolución!</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Coro:</h4>
            <p>¡BeatGenius, dale play!<br>
            IA y música, ganarás.<br>
            Concursos, premios, fama y más,<br>
            ¡el futuro suena, ven a crear!</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 2:</h4>
            <p>Desde cero a pro, sin estudiar solfeo,<br>
            la máquina ayuda, pero el flow es mío.<br>
            Vendo beats en la app, royalties al firmar,<br>
            oigo mi tema en la radio, ¡qué más puedo pedir!<br><br>
            Sellos discográficos miran mi perfil,<br>
            la plataforma me lanza, no necesito un manager.<br>
            TikTok, Instagram, mi sonido viral,<br>
            ¡gracias a la IA, ahora soy el king!</p>
        </div>
        
        <div class="bridge">
            <h4 style="color: #E67E22;">Puente:</h4>
            <p>Generado en BeatGenius, copyright compartido,<br>
            70% pa’ la empresa, 30% pa’ tu bolsillo...</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Coro (Repetición):</h4>
            <p>¡BeatGenius, dale play!<br>
            IA y música, ganarás.<br>
            Concursos, premios, fama y más,<br>
            ¡el futuro suena, ven a crear!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h3 style="color: #E74C3C;">🎤 Karaoke Time! 🎤</h3>
        <p>¡Sigue la letra mientras suena la música!</p>
        <div style="height: 10px;"></div>
        <img src="https://cdn.pixabay.com/photo/2020/04/12/01/58/microphone-5032177_640.jpg" style="width: 100%; max-width: 400px; border-radius: 10px;" class="interactive">
    </div>
    """, unsafe_allow_html=True)
