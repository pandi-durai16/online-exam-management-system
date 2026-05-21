from flask import Blueprint, render_template
from utils.db import get_db

# ✅ DEFINE BLUEPRINT FIRST
result_bp = Blueprint("result", __name__)

# ---------------- RESULT PAGE ----------------
@result_bp.route("/result/<int:sid>")
def result(sid):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT percentage FROM results WHERE student_id=?", (sid,))
    row = cur.fetchone()
    score = row["percentage"] if row else 0

    cur.execute("""
        SELECT q.question, q.a, q.b, q.c, q.d,
               q.correct, a.selected
        FROM questions q
        JOIN answers a ON q.id = a.question_id
        WHERE a.student_id = ?
    """, (sid,))

    details = cur.fetchall()
    db.close()

    return render_template(
        "result.html",
        score=score,
        details=details
    )


# ---------------- LEADERBOARD ----------------
@result_bp.route("/leaderboard/<int:subject_id>")
def leaderboard(subject_id):
    db = get_db()
    cur = db.cursor()

    cur.execute("""
        SELECT u.username, r.percentage
        FROM results r
        JOIN users u ON u.id = r.student_id
        WHERE r.subject_id = ?
        ORDER BY r.percentage DESC
    """, (subject_id,))

    leaders = cur.fetchall()

    cur.execute("SELECT name FROM subjects WHERE id=?", (subject_id,))
    subject = cur.fetchone()["name"]

    db.close()

    return render_template(
        "leaderboard.html",
        leaders=leaders,
        subject=subject
    )
