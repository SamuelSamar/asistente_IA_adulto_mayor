import os
from groq import Groq
from config.settings import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def generate_response_groq(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model = GROQ_MODEL,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error REAL de Groq: {e}")
        return "Actualmente no puedo responder (Error de conexión con Groq)."