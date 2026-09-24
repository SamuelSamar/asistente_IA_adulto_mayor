# Crear conexion SQLite
import sqlite3
from pathlib import Path

DATABASE_PATH = Path("database/asistente.db")

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT,
        message TEXT, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        age INTEGER,
        medications TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    connection.commit()
    connection.close()