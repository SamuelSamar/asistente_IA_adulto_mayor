import speech_recognition as sr
from openai import OpenAI
from gtts import gTTS

def transcribir_audio(ruta_archivo):
    reconocedor = sr.Recognizer()
    try:
        with sr.AudioFile(ruta_archivo) as fuente:
            audio_data = reconocedor.record(fuente)
            texto = reconocedor.recognize_google(audio_data, language="es-PE")
            return texto
    except sr.UnknownValueError:
        print("El servicio de Google no puedo entender el audio.")
        return None
    except sr.RequestError as e:
        print(f"Error de conexión con el servicio de Google: {e}")
        return None
    except Exception as e:
        print(f"Error en transcripción: {e}")
        return None

def texto_a_audio(texto, ruta_salida="respuesta_asistente.mp3"):
    try:
        tts = gTTS(text=texto, lang='es')
        tts.save(ruta_salida)
        return ruta_salida
    except Exception as e:
        print(f"Error al generar audio: {e}")
        return None