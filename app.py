import streamlit as st
from gtts import gTTS
import os
from io import BytesIO

# Page configuration
st.set_page_config(page_title="Text to Speech (gTTS)", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🗣️ Text to Speech (gTTS)</h1>", unsafe_allow_html=True)
st.markdown("Convert your Spanish text into spoken audio easily.")

# Form layout
with st.form("tts_form"):
    text = st.text_area("📝 Enter your text (in Spanish):", "Hola, ¿cómo estás?")
    lang = st.selectbox("🌐 Select language:", ["es"], help="Currently only Spanish is supported.")
    submitted = st.form_submit_button("🎧 Convert and Play")

# Handle form submission
if submitted:
    if not text.strip():
        st.error("⚠️ Please enter some text before converting.")
    else:
        # Convert text to speech
        tts = gTTS(text, lang=lang)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        
        st.success("✅ Conversion successful! Listen below:")
        st.audio(mp3_fp, format="audio/mp3")
        st.markdown("---")
        st.info("Powered by gTTS (Google Text-to-Speech)")

