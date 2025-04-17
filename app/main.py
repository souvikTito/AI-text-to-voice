import os
from dotenv import load_dotenv
from ollama_client import get_ollama_response
from elevenlabs_client import text_to_speech

load_dotenv()

def run_cli():
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            ai_response = get_ollama_response(user_input)
            print("AI:", ai_response)
            text_to_speech(ai_response)
    except KeyboardInterrupt:
        print("\nExiting gracefully...")

if __name__ == "__main__":
    print("API Key Loaded:", bool(os.getenv("ELEVENLABS_API_KEY")))
    run_cli()