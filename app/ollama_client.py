import os
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_ollama_response(prompt: str) -> str:
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "llama3"),
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "Error: No response")