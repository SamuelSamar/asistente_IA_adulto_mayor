import smtplib
# from email.mime.text import MIMEText
from email.message import EmailMessage
from config.settings import EMAIL_SENDER, EMAIL_PASSWORD
from services.database_service import get_profile

def enviar_email_cuidador(user_id, nombre_paciente, correo_destino):
    perfil = get_profile(user_id)

    if not perfil or not perfil.get("medications"):
        return False, "No hay medicamentos registrados para este usuario"

    medicamentos = perfil["medications"]
    edad = perfil["age"]

    # Armar el cuerpo del mensaje usando comillas triples
    contenido = f"""Hola,
    Este es un reporte automático del Asistente Virtual para Adultos Mayores.
    Datos del paciente:
    - Nombre: {nombre_paciente}
    - Edad: {edad} años

    Los medicamentos registrados y recordatorios actuales son:
    {medicamentos}
    
    Saludos cordiales,
    Sistema de Asistencia IA"""

    mensaje = EmailMessage()
    mensaje.set_content(contenido)
    mensaje['Subject'] = "Reporte de Salud y Medicación - Asistente IA"
    mensaje['From'] = EMAIL_SENDER
    mensaje['To'] = correo_destino

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, correo_destino, mensaje.as_string())
        return True, "Correo de alerta enviado exitosamente al familiar."
    except Exception as e:
        return False, f"Error al enviar el correo: {e}"