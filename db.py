import sqlite3
from datetime import datetime

DB_NAME = "academic_agent.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        user_input TEXT,
        action TEXT,
        output TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_interaction(session_id, user_input, action, output):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interactions (session_id, user_input, action, output, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        session_id,
        user_input,
        action,
        output,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

def get_past_interactions(session_id, limit=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_input, action, timestamp
    FROM interactions
    WHERE session_id = ?
    ORDER BY id DESC
    LIMIT ?
    """, (session_id, limit))

    rows = cursor.fetchall()
    conn.close()
    return rows
