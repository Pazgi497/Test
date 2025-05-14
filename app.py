import streamlit as st
from gtts import gTTS
import os
import time
from playsound import playsound

# Streamlit App Layout
st.title('Text-to-Speech (TTS) Demo')

st.subheader("Test different TTS Settings")

# Input text box for user
text_input = st.text_area("Enter the text for TTS", "¡Hola! ¿Cómo estás?", height=150)

# Language selection
language = st.selectbox("Select Language", ["es", "en", "fr", "de"], index=0)

# Speech Rate
rate = st.slider("Speech Rate", min_value=50, max_value=200, value=120, step=10)

# Output file path
output_file = "tts_output.mp3"

# Function to generate TTS audio
def generate_tts(text, lang, speed, output_file):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)  # gTTS does not take speed directly
        tts.save(output_file)
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Generate audio when the button is clicked
if st.button("Generate and Play Audio"):
    with st.spinner('Generating audio...'):
        time.sleep(2)  # Simulating some delay in audio generation

        # Generate TTS
        if generate_tts(text_input, language, rate, output_file):
            st.success("Audio Generated Successfully!")

            # Play Audio
            st.audio(output_file, format="audio/mp3")
            
            # Download option
            st.download_button(
                label="Download the Audio",
                data=open(output_file, "rb").read(),
                file_name="generated_audio.mp3",
                mime="audio/mp3"
            )
        else:
            st.error("Something went wrong while generating the audio.")
