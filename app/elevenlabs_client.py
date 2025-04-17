import os
import re
import requests
from utils.audio_utils import play_audio

# Get voice ID from environment or use default
VOICE_ID = os.getenv("VOICE_ID", "21m00Tcm4TlvDq8ikWAM")  # Default Rachel voice
ELEVENLABS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

def clean_markdown(text: str) -> str:
    """Remove Markdown formatting"""
    text = re.sub(r'\*\*(.*?)\*\*|__(.*?)__', r'\1\2', text)
    text = re.sub(r'\*(.*?)\*|_(.*?)_', r'\1\2', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    return text.strip()

def text_to_speech(text: str):
    headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        "Content-Type": "application/json",
        "accept": "audio/mpeg"
    }
    data = {
        "text": clean_markdown(text),
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.8
        }
    }
    response = requests.post(ELEVENLABS_URL, headers=headers, json=data)
    if response.status_code == 200:
        play_audio(response.content)
    else:
        raise Exception(f"ElevenLabs Error {response.status_code}: {response.text}")