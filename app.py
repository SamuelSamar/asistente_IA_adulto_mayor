import streamlit as st
from ui.chat_ui import render_chat
from services.chatbot_service import chat
from database.database import create_tables
from services.database_service import (save_message, get_history, get_or_create_user, save_profile, get_profile)
from ui.profile_ui import render_profile_form
from services.email_service import enviar_email_cuidador
from services.sheets_service import registrar_chat, registrar_perfil
from services.audio_service import transcribir_audio, texto_a_audio

create_tables()

st.set_page_config(page_title="Asistente IA", page_icon="🤖")

user_id = get_or_create_user()

st.sidebar.header("Notificar al Cuidador")
correo_familiar = st.sidebar.text_input("Correo del familiar cuidador:")

perfil = render_profile_form()

if perfil["guardar"]:
    nombre_final = perfil["nombre"] if perfil["nombre"] else "Adulto Mayor"
    user_id = get_or_create_user(nombre_final)

    save_profile(user_id, perfil["age"], perfil["medications"])
    st.success(f"Perfil de {nombre_final} guardado correctamente.")

    registrar_perfil(nombre_final, perfil["age"], perfil["medications"])

    if correo_familiar:
        exito, msg = enviar_email_cuidador(user_id, nombre_final, correo_familiar)
        if exito:
            st.info("Se ha enviado el nuevo perfil al correo y se registró en la bitácora")
        else:
            st.error(f"Error al enviar correo: {msg}")

mensaje_texto, mensaje_voz = render_chat()
if "audio_pendiente" in st.session_state and st.session_state.audio_pendiente:
    st.audio(st.session_state.audio_pendiente, format="audio/mp3", autoplay=True)
    st.session_state.audio_pendiente = None

mensaje_final = None

if mensaje_texto:
    mensaje_final = mensaje_texto
elif mensaje_voz:
    with open("temp_audio.wav", "wb") as f:
        f.write(mensaje_voz.getbuffer())
    with st.spinner("Escuchando..."):
        mensaje_final = transcribir_audio("temp_audio.wav")

if mensaje_final:
    save_message(user_id, "user", mensaje_final)
    registrar_chat("Usuario", mensaje_final)

    st.session_state.messages.append({"role":"user", "content":mensaje_final})

    historial = get_history(user_id)
    respuesta = chat(mensaje_final, historial, user_id)

    save_message(user_id, "assistant", respuesta)
    registrar_chat("Asistente", respuesta)

    st.session_state.messages.append({"role": "assistant", "content":respuesta})

    archivo_audio = texto_a_audio(respuesta)
    if archivo_audio:
        st.session_state.audio_pendiente = archivo_audio

    if mensaje_voz:
        st.session_state.audio_key += 1

    st.rerun()