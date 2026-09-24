# De respaldo
# from core.gemini_client import generate_response

# Importacion Groq
from core.groq_client import generate_response_groq
from services.database_service import get_profile

def chat(message, history, user_id):
    contexto = """
    Eres un asistente virtual especializado
    en ayudar a adultos mayores.

    Características:
    - Usa lenguaje sencillo.
    - Sé paciente y amable.
    - Evita términos técnicos.
    - Brinda orientación clara.
    """

    profile = get_profile(user_id)

    perfil_texto = ""

    if profile:
        perfil_texto = f"""
        Información del adulto mayor:
        Edad:{profile['age']}
        Medicamentos:{profile['medications']}
        """

    conversacion = (
        contexto
        +
        "\n"
        +
        perfil_texto
        +
        "\nHistorial de conversación:\n"
    )

    for item in history:
        conversacion += (f"{item['role']}: "
                         f"{item['content']}\n")

    conversacion += ("\nUsuario:" + message +"\nAsistente:")

    # return generate_response(conversacion)
    return generate_response_groq(conversacion)