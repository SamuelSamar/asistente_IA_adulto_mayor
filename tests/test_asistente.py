import os
from database.database import create_tables
from services.database_service import get_or_create_user, save_profile, get_profile
from config.settings import GROQ_MODEL
from pathlib import Path
from database.database import DATABASE_PATH

def test_registro_perfil_base_datos():
    os.makedirs("database", exist_ok=True)
    create_tables()
    user_id = get_or_create_user("UsuarioPrueba")
    edad_prueba = 80
    meds_prueba = "Aspirina 100mg, Losartán"
    save_profile(user_id, edad_prueba, meds_prueba)
    perfil_recuperado = get_profile(user_id)

    assert perfil_recuperado is not None, "El perfil no se guardó en la base de datos"
    assert perfil_recuperado["age"] == edad_prueba, "La edad registrada no coincide"
    assert perfil_recuperado["medications"] == meds_prueba, "Los medicamentos no coinciden"

def test_modelo_groq_configurado():
    modelo_esperado = "llama-3.1-8b-instant"
    assert GROQ_MODEL == modelo_esperado, f"Configuración errónea. Esperado: {modelo_esperado}, Actual: {GROQ_MODEL}"

def test_database_path_format():
    assert isinstance(DATABASE_PATH, Path), "La ruta de la BD debe ser un objeto Path"
    assert DATABASE_PATH.suffix == '.db', "La base de datos debe tener extensión .db"