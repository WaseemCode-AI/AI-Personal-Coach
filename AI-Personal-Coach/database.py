import sqlite3

conn = sqlite3.connect("user_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    goal TEXT,
    progress INTEGER
)
""")

conn.commit()
conn.close()

def add_user(name, goal):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, goal, progress) VALUES (?, ?, ?)", (name, goal, 0))
    conn.commit()
    conn.close()

def update_progress(name, progress):
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET progress = ? WHERE name = ?", (progress, name))
    conn.commit()
    conn.close()
