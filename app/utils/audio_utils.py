import os
import io
import sounddevice as sd
import soundfile as sf

def play_audio(audio_bytes: bytes):
    """Handle all audio operations including saving and playback"""
    try:
        # Create assets directory if needed
        os.makedirs("assets", exist_ok=True)
        
        # Save to file (for Streamlit)
        with open("assets/output.mp3", "wb") as f:
            f.write(audio_bytes)
            
        # Play audio
        with io.BytesIO(audio_bytes) as audio_file:
            data, sample_rate = sf.read(audio_file)
            sd.play(data, sample_rate)
            sd.wait()
            
    except Exception as e:
        print(f"Audio error: {e}")
        raise  # Re-raise to handle in calling code