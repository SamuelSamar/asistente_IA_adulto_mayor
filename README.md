# Asistente Inteligente IA para Adultos Mayores 🤖

Este es un asistente conversacional basado en inteligencia artificial diseñado para ayudar a adultos mayores. Utiliza procesamiento de lenguaje natural (Groq/Gemini), reconocimiento de voz gratuito de Google y guarda registros automáticos en Google Sheets.

## 🚀 Requisitos Previos
1. Python 3.9 o superior instalado.
2. Una cuenta de Google (para los registros en Sheets y notificaciones por correo).

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd asistente_adulto_mayor_ia
```

2. Crea y activa un entorno virtual:
```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Mac/Linux:
source .venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🔐 Configuración de Variables de Entorno (.env)

Debes crear un archivo llamado `.env` en la raíz del proyecto. Llena los datos siguiendo estos pasos:

1. **GROQ_API_KEY:** Crea una cuenta en [Groq Console](https://console.groq.com/keys) y genera una nueva API Key.
2. **GEMINI_API_KEY:** (Opcional, de respaldo). Obtenla en [Google AI Studio](https://aistudio.google.com/app/apikey).
3. **EMAIL_SENDER y EMAIL_PASSWORD:** 
   - Usa tu dirección de Gmail normal para `EMAIL_SENDER`.
   - Para `EMAIL_PASSWORD`, **no uses tu contraseña habitual**. Ve a la configuración de tu cuenta de Google -> Seguridad -> Verificación en dos pasos -> **Contraseñas de aplicaciones**. Genera una nueva contraseña para "Correo" y pega esos 16 caracteres aquí.

```env
GROQ_API_KEY=tu_clave_de_groq
GEMINI_API_KEY=tu_clave_de_gemini
EMAIL_SENDER=tu_correo@gmail.com
EMAIL_PASSWORD=tu_contraseña_de_aplicacion
```

## 📊 Configuración de Google Sheets (.json)

El sistema guarda la bitácora del chat y los perfiles en Google Sheets. Para que funcione localmente, necesitas un archivo de credenciales:

1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un nuevo proyecto y habilita la **Google Sheets API** y **Google Drive API**.
3. Ve a "Credenciales" > Crear Credenciales > **Cuenta de Servicio** (Service Account).
4. Una vez creada, entra a la cuenta de servicio, ve a la pestaña "Claves" (Keys) > Agregar clave > Crear nueva clave > formato **JSON**.
5. Descarga el archivo, renómbralo a `ocr-ruc-9bb6b695ec5d.json` y guárdalo en la raíz de este proyecto.
6. **Muy importante:** Abre el archivo JSON, copia el correo de la cuenta de servicio (termina en `@tu-proyecto.iam.gserviceaccount.com`) y ve a tu Google Drive. Crea dos hojas de cálculo llamadas `BITACORA-ASISTENTE IA` y `PERFILES-ASISTENTE IA` y compártelas como **Editor** con ese correo.

## ▶️ Ejecución

Una vez configurado todo, levanta la aplicación con Streamlit:
```bash
streamlit run app.py
```