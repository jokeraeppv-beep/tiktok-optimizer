import streamlit as st
import ffmpeg
import os

# ==========================================
# 1. CONFIGURATION DE L'INTERFACE
# ==========================================
st.set_page_config(
    page_title="Method Upload Joker v7.0 - Multi-FPS Selector",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style Custom Cyberpunk
st.markdown("""
    <style>
    .main { background-color: #020307; color: #f0f2f6; font-family: 'Helvetica Neue', Arial, sans-serif; }
    h1 { background: linear-gradient(45deg, #00f2fe, #7928ca, #ff007f); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900 !important; }
    .stFileUploader { border: 2px dashed #00f2fe; background-color: #050611; border-radius: 14px; padding: 25px; }
    .stButton>button { 
        background: linear-gradient(45deg, #00f2fe, #7928ca, #ff007f); 
        background-size: 200% auto; color: white !important; font-weight: bold; font-size: 16px !important;
        border: none !important; border-radius: 12px; padding: 14px 35px !important;
        box-shadow: 0 5px 20px rgba(255, 0, 127, 0.3); transition: all 0.3s ease-in-out;
        width: 100%;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0, 242, 254, 0.4); background-position: right center; }
    .stVideo { border-radius: 14px; overflow: hidden; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.8); border: 1px solid #16192e; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Method Joker v7.0 : Multi-FPS Selector")
st.markdown("<p style='color: #555d80; font-size: 15px;'>Choisis ta fluidité dans le menu déroulant et applique ta commande itsscale instantanément.</p>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 2. MENU DÉROULANT DU CHOIX FPS
# ==========================================
fps_choice = st.selectbox(
    "🚀 SÉLECTIONNE LE MODE DE FLUIDITÉ POUR TIKTOK :",
    ["60 FPS (Script itsscale 2)", "120 FPS (Script itsscale 6)"]
)

# ==========================================
# 3. ZONE D'UPLOAD
# ==========================================
uploaded_file = st.file_uploader("🛸 Dépose ton master 1080x1080", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    original_name = uploaded_file.name
    name_without_ext, ext = os.path.splitext(original_name)
    
    # Détermination automatique des variables selon ton choix dans le menu
    if "120 FPS" in fps_choice:
        scale_val = 6
        suffix = "120fps"
    else:
        scale_val = 2
        suffix = "60fps"
        
    output_filename = f"{name_without_ext}_{suffix}_itsscale.mp4"
    
    input_temp_path = "input_temp_processing.mp4"
    output_temp_path = "output_temp_processing.mp4"

    with open(input_temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.subheader("📺 CLIP SOURCE")
    st.video(input_temp_path)
    st.markdown("---")
    
    # Le bouton s'adapte dynamiquement au choix sélectionné
    if st.button(f"🚀 LANCER LA COPIE BRUTE DIRECTE ({suffix.upper()})"):
        if os.path.exists(output_temp_path):
            os.remove(output_temp_path)
            
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.markdown(f"<p style='color: #00f2fe;'>Injection de la commande brute : -itsscale {scale_val}...</p>", unsafe_allow_html=True)
        progress_bar.progress(50)
        
        try:
            # Traduction exacte de tes deux lignes de commande selon l'option choisie
            (
                ffmpeg
                .input(input_temp_path, itsscale=scale_val)
                .output(output_temp_path, vcodec='copy', acodec='copy')
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            
            progress_bar.progress(100)
            status_text.markdown(f"<p style='color: #00ff7f;'>🎯 FLUIDITÉ {suffix.upper()} APPLIQUÉE EN MOINS D'UNE SECONDE !</p>", unsafe_allow_html=True)
            st.balloons()
            
            st.subheader("🔥 RENDU INSTANTANÉ")
            st.video(output_temp_path)
            
            with open(output_temp_path, "rb") as file:
                st.download_button(
                    label=f"📥 TÉLÉCHARGER LE CLIP {suffix.upper()}",
                    data=file,
                    file_name=output_filename,
                    mime="video/mp4"
                )
                
        except ffmpeg.Error as e:
            st.error("Erreur de traitement. Vérifie que le fichier source n'est pas corrompu.")
            st.text(e.stderr.decode('utf8'))
        
        finally:
            if os.path.exists(input_temp_path):
                os.remove(input_temp_path)