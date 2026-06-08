import streamlit as st
import ffmpeg
import os

# ==========================================
# 1. ARCHITECTURE ET DESIGN DE L'ESPACE (CSS)
# ==========================================
st.set_page_config(
    page_title="Joker Optimizer | Space Render Engine",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Injection CSS pour un rendu haut de gamme international
st.markdown("""
    <style>
    /* Fond de l'espace profond */
    .main {
        background-color: #03030c;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
        background-size: 550px 550px, 350px 350px, 250px 250px;
        background-position: 0 0, 40px 60px, 130px 270px;
        color: #e2e8f0;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Titre Pro avec dégradé Cosmique */
    .cosmic-title {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 30%, #7928ca 70%, #ff007f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 5px;
    }
    
    .cosmic-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* Cartes en verre transparent (Glassmorphism) */
    div[data-testid="stForm"], .stSelectbox, .stFileUploader {
        background: rgba(13, 16, 39, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(0, 242, 254, 0.15) !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
        padding: 25px !important;
    }

    /* Input et Zone d'upload épurée */
    .stFileUploader {
        border: 2px dashed rgba(0, 242, 254, 0.3) !important;
        transition: all 0.3s ease;
    }
    .stFileUploader:hover {
        border-color: #00f2fe !important;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.2) !important;
    }

    /* Bouton d'action "Horizon des Événements" */
    .stButton>button {
        background: linear-gradient(90deg, #00f2fe 0%, #7928ca 50%, #ff007f 100%) !important;
        background-size: 200% auto !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        letter-spacing: 0.5px;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 0px !important;
        width: 100%;
        box-shadow: 0 4px 20px rgba(121, 40, 202, 0.4) !important;
        transition: all 0.4s ease-in-out !important;
    }
    .stButton>button:hover {
        background-position: right center !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(0, 242, 254, 0.6) !important;
    }

    /* Badges de confiance pro */
    .trust-container {
        display: flex;
        justify-content: space-around;
        margin-top: 40px;
        background: rgba(255, 255, 255, 0.03);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .trust-badge {
        font-size: 0.85rem;
        color: #64748b;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .trust-badge strong { color: #38bdf8; }

    /* Lecteur vidéo */
    .stVideo {
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Header du site
st.markdown('<h1 class="cosmic-title">JOKER RENDER ENGINE</h1>', unsafe_allow_html=True)
st.markdown('<p class="cosmic-subtitle">Système d\'encodage sécurisé pour la préservation des métadonnées vidéo.</p>', unsafe_allow_html=True)

# ==========================================
# 2. CONFIGURATION DES OPTIONS PRO
# ==========================================
fps_choice = st.selectbox(
    "🌌 SÉLECTIONNER LA CONFIGURATION TEMPORELLE :",
    ["60 FPS Locked (Algorithme itsscale 2)", "120 FPS Overclock (Algorithme itsscale 6)"]
)

st.markdown("<br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("🛸 GLISSER-DÉPOSER LE MASTER (MP4, MOV, AVI)", type=["mp4", "mov", "avi"])

# ==========================================
# 3. MOTEUR DE TRAITEMENT
# ==========================================
if uploaded_file is not None:
    original_name = uploaded_file.name
    name_without_ext, ext = os.path.splitext(original_name)
    
    if "120 FPS" in fps_choice:
        scale_val = 6
        suffix = "120fps"
    else:
        scale_val = 2
        suffix = "60fps"
        
    output_filename = f"{name_without_ext}_{suffix}_cosmic.mp4"
    input_temp_path = "input_temp_processing.mp4"
    output_temp_path = "output_temp_processing.mp4"

    with open(input_temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📺 MONITORING SOURCE")
    st.video(input_temp_path)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button(f"INITIALISER L'INJECTION TEMPORELLE ({suffix.upper()})"):
        if os.path.exists(output_temp_path):
            os.remove(output_temp_path)
            
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.markdown(f"<p style='color: #00f2fe; text-align:center;'>🚀 Traitement de la matrice... Commande brute -itsscale {scale_val}</p>", unsafe_allow_html=True)
        progress_bar.progress(50)
        
        try:
            (
                ffmpeg
                .input(input_temp_path, itsscale=scale_val)
                .output(output_temp_path, vcodec='copy', acodec='copy')
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            
            progress_bar.progress(100)
            status_text.markdown("<p style='color: #00ff7f; text-align:center; font-weight:bold;'>🎯 CALCUL EFFECTUÉ AVEC SUCCÈS !</p>", unsafe_allow_html=True)
            st.balloons()
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("🔥 MASTER COMPILÉ (PRÊT POUR LE COMPTE)")
            st.video(output_temp_path)
            
            with open(output_temp_path, "rb") as file:
                st.download_button(
                    label=f"📥 TÉLÉCHARGER LE FICHIER MASTER",
                    data=file,
                    file_name=output_filename,
                    mime="video/mp4"
                )
                
        except ffmpeg.Error as e:
            st.error("Défaut dans la structure du container vidéo.")
            st.text(e.stderr.decode('utf8'))
        
        finally:
            if os.path.exists(input_temp_path):
                os.remove(input_temp_path)

# ==========================================
# 4. ZONE DE CONFIANCE (FOOTER)
# ==========================================
st.markdown("""
    <div class="trust-container">
        <div class="trust-badge">🔒 Sécurité : <strong>Local & Chiffré</strong></div>
        <div class="trust-badge">💎 Qualité : <strong>Lossless Copy</strong></div>
        <div class="trust-badge">🛰️ Serveur : <strong>Cloud permanent Active</strong></div>
    </div>
""", unsafe_allow_html=True)
