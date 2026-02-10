from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

DB_NAME = "gramata.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS gramatas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT,
            autors TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()

