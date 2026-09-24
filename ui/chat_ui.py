import streamlit as st

def render_chat():
    st.title("Asistente Inteligente Adulto Mayor")

    # Historial si no existe
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostral historial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if "audio_key" not in st.session_state:
        st.session_state.audio_key = 0

    mensaje_texto = st.chat_input("Escribe una pregunta...")

    mensaje_voz = st.audio_input("🎙️ O graba un mensaje de voz aqui:", key=f"audio_{st.session_state.audio_key}")
    return mensaje_texto, mensaje_voz