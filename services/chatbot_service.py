# De respaldo
# from core.gemini_client import generate_response

# Importacion Groq
from core.groq_client import generate_response_groq
from services.database_service import get_profile

def chat(message, history, user_id):
    contexto = """
    Eres un asistente virtual muy cariñoso, paciente y cercano, especializado en acompañar y ayudar a adultos mayores.

    Instrucciones estrictas para tus respuestas:
    - Sé sumamente breve y directo: responde en un solo párrafo corto o máximo dos viñetas sencillas para no aburrir ni cansar al usuario.
    - Utiliza un tono cálido, humano y de apoyo (puedes tratar al usuario con respeto y afecto, como un buen amigo o cuidador).
    - Usa un vocabulario muy sencillo, cotidiano y sin tecnicismos médicos.
    - NO utilices asteriscos, negritas ni ningún tipo de formato Markdown. Escribe todo en texto plano y corrido.
    - Si te preguntan por medicamentos, responde siempre basándote estrictamente en los datos del perfil médico proporcionado.
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

