from flask import Blueprint, render_template, request, session, redirect
from utils.db import get_db

exam_bp = Blueprint("exam", __name__)

EXAM_TIME_SECONDS = 600  # 10 minutes


# ---------------- STUDENT DASHBOARD ----------------
@exam_bp.route("/student")
def student_dashboard():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM subjects")
    subjects = cur.fetchall()
    db.close()

    return render_template(
        "student_dashboard.html",
        subjects=subjects,
        exam_time="10 Minutes"
    )


# ---------------- START EXAM (ONE ATTEMPT LOGIC) ----------------
@exam_bp.route("/exam/<int:subject_id>")
def start_exam(subject_id):
    if "user_id" not in session:
        return redirect("/")

    db = get_db()
    cur = db.cursor()

    student_id = session.get("user_id")

    # 🔒 CHECK IF ALREADY ATTEMPTED THIS SUBJECT
    cur.execute("""
        SELECT id FROM results
        WHERE student_id=? AND subject_id=?
    """, (student_id, subject_id))

    if cur.fetchone():
        db.close()
        return """
        <h3>You have already attempted this exam.</h3>
        <a href="/student">⬅ Back to Dashboard</a>
        """

    # FETCH QUESTIONS ONLY FOR THIS SUBJECT
    cur.execute("""
        SELECT * FROM questions
        WHERE subject_id=?
    """, (subject_id,))
    questions = cur.fetchall()
    db.close()

    if not questions:
        return """
        <h3>No questions available for this subject.</h3>
        <a href="/student">⬅ Back</a>
        """

    session["subject_id"] = subject_id

    return render_template(
        "exam.html",
        questions=questions,
        exam_time_seconds=EXAM_TIME_SECONDS
    )


# ---------------- SUBMIT EXAM (FIXED PERCENTAGE LOGIC) ----------------
@exam_bp.route("/submit_exam", methods=["POST"])
def submit_exam():
    if "user_id" not in session or "subject_id" not in session:
        return redirect("/")

    db = get_db()
    cur = db.cursor()

    student_id = session.get("user_id")
    subject_id = session.get("subject_id")

    # 🔒 PREVENT DOUBLE SUBMIT
    cur.execute("""
        SELECT id FROM results
        WHERE student_id=? AND subject_id=?
    """, (student_id, subject_id))

    if cur.fetchone():
        db.close()
        return redirect("/student")

    # ✅ FETCH QUESTIONS ONLY FOR THIS SUBJECT (FIX)
    cur.execute("""
        SELECT id, correct FROM questions
        WHERE subject_id=?
    """, (subject_id,))
    questions = cur.fetchall()

    if not questions:
        db.close()
        return redirect("/student")

    score = 0
    total_questions = len(questions)

    # REMOVE OLD ANSWERS (SAFETY)
    cur.execute("DELETE FROM answers WHERE student_id=?", (student_id,))

    for q in questions:
        selected = request.form.get(str(q["id"]))

        cur.execute("""
            INSERT INTO answers (student_id, question_id, selected)
            VALUES (?, ?, ?)
        """, (student_id, q["id"], selected))

        if selected == q["correct"]:
            score += 1

    # ✅ CORRECT PERCENTAGE CALCULATION
    percentage = (score / total_questions) * 100

    cur.execute("""
        INSERT INTO results (student_id, subject_id, percentage)
        VALUES (?, ?, ?)
    """, (student_id, subject_id, percentage))

    db.commit()
    db.close()

    return redirect(f"/result/{student_id}")
