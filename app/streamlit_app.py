import os
import time
import streamlit as st
from dotenv import load_dotenv
from ollama_client import get_ollama_response
from elevenlabs_client import text_to_speech

# Initialize
load_dotenv()
os.makedirs("assets", exist_ok=True)

# Streamlit UI
st.set_page_config(page_title="AI Voice Assistant", page_icon="🤖")
st.title("Ollama + ElevenLabs Voice Assistant")

# Session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What would you like to discuss?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.spinner("Thinking..."):
        try:
            ai_response = get_ollama_response(prompt)  # Now properly defined
            
            # Add AI response to history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
            # Display AI response
            with st.chat_message("assistant"):
                st.markdown(ai_response)
            
            # Generate and display audio
            try:
                text_to_speech(ai_response)
                time.sleep(0.5)  # Brief delay for file writing
                
                if os.path.exists("assets/output.mp3"):
                    with open("assets/output.mp3", "rb") as audio_file:
                        st.audio(audio_file.read(), format="audio/mp3")
                else:
                    st.warning("AI responded but audio couldn't be generated")
                    
            except Exception as audio_error:
                st.error(f"Audio generation failed: {str(audio_error)}")
                
        except Exception as ai_error:
            st.error(f"AI response failed: {str(ai_error)}")