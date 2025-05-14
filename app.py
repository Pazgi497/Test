from gtts import gTTS
import os
from playsound import playsound

# Your Spanish script text
spanish_script = """
Bienvenido a TruckMetrics video

Esta es una sesión de capacitación del MetricsManager Pro, diseñada para brindarte instrucciones claras.
Específicamente, para usuarios de MetricsManager Pro que han instalado TruckMetrics en sus sitios.

Ten en cuenta que esta capacitación no incluye hardware ni información de instalación, para eso, 
consulta el manual de TruckMetrics, que puedes encontrar adjunto en este artículo. 

La agenda de hoy abarca los módulos disponibles en TruckMetrics, 
incluyendo las características en MetricsManager Pro, como el tablero, distribución de tamaño de partícula, PSD, productividad y reportabilidad de la galería. 
"""

# Function to generate audio
def generate_audio(text, output_file):
    try:
        # Generate TTS audio
        tts = gTTS(text=text, lang='es')
        tts.save(output_file)
        print(f"✅ Audio dubbing saved as: {output_file}")
        
        # Play the audio file
        playsound(output_file)
        print("✅ Audio played successfully.")
        
    except Exception as e:
        print(f"❌ Error generating or playing TTS: {e}")

# File path for saved audio
output_file = "dubbing_output.mp3"

# Check if the output file already exists, if yes, delete it
if os.path.exists(output_file):
    os.remove(output_file)

# Generate and play the audio
generate_audio(spanish_script, output_file)
