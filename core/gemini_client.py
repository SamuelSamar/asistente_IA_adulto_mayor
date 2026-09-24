from google import genai

from config.settings import (GEMINI_API_KEY, MODEL_NAME)

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt):
    try:
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        return response.text
    except Exception as e:
        return ("Actualmente no puedo responder")