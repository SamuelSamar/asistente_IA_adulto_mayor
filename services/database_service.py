from database.database import get_connection

def save_message(user_id, role, message):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO conversations (user_id, role, message)
        VALUES (?, ?, ?)
        """,
        (user_id, role, message)
    )
    connection.commit()
    connection.close()

def get_history(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT role, message
        FROM conversations
        WHERE user_id = ?
        ORDER BY id ASC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()
    connection.close()
    history = []

    for role, message in rows:
        history.append(
            {
                "role": role,
                "content": message
            }
        )
    return history

def get_or_create_user(name="Carlos"):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE name = ?
        """, (name,)
    )
    user = cursor.fetchone()

    if user:
        user_id = user[0]
    else:
        cursor.execute(
            """
            INSERT INTO users(name)
            VALUES(?)
            """, (name,)
        )
        user_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return user_id

def save_profile(user_id, age, medications):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT OR REPLACE INTO profiles
        (
            user_id,
            age,
            medications
        )
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            age,
            medications,
        )
    )
    connection.commit()
    connection.close()

def get_profile(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT
            age,
            medications
        FROM profiles
        WHERE user_id = ?
        """,
        (user_id,)
    )
    profile = cursor.fetchone()
    connection.close()

    if profile:
        return {
            "age": profile[0],
            "medications": profile[1]
        }
    
    return None