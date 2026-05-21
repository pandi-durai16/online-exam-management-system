import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "online_exam.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_id INTEGER,
        question TEXT,
        a TEXT, b TEXT, c TEXT, d TEXT,
        correct TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        percentage REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS answers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        question_id INTEGER,
        selected TEXT
    )
    """)

    conn.commit()
    return conn


# ---------- RUN ONCE ----------
if __name__ == "__main__":
    db = get_db()
    cur = db.cursor()

    # ADMIN
    cur.execute("""
    INSERT INTO users (username, password, role)
    VALUES ('admin', 'admin123', 'admin')
    """)

    # STUDENT
    cur.execute("""
    INSERT INTO users (username, password, role)
    VALUES ('student', '123', 'student')
    """)

    # SUBJECTS
    cur.execute("INSERT INTO subjects (name) VALUES ('Python')")
    cur.execute("INSERT INTO subjects (name) VALUES ('Java')")

    db.commit()
    db.close()
    print("✅ Database created with admin & student")
