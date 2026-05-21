from flask import Blueprint, render_template, request, redirect, session
from utils.db import get_db
import sqlite3

admin_bp = Blueprint("admin", __name__)

# ---------------- ADMIN DASHBOARD ----------------
@admin_bp.route("/admin")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect("/")
    return render_template("admin_dashboard.html")


# ---------------- ADD STUDENT ----------------
@admin_bp.route("/admin/add-student", methods=["GET", "POST"])
def add_student():
    if session.get("role") != "admin":
        return redirect("/")

    error = None
    db = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            db = get_db()
            cur = db.cursor()
            cur.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, 'student')",
                (username, password)
            )
            db.commit()
            return redirect("/admin/students")

        except sqlite3.IntegrityError:
            error = "Username already exists!"

        finally:
            if db:
                db.close()

    return render_template("add_student.html", error=error)


# ---------------- VIEW STUDENTS ----------------
@admin_bp.route("/admin/students")
def view_students():
    if session.get("role") != "admin":
        return redirect("/")

    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, username FROM users WHERE role='student'")
    students = cur.fetchall()
    db.close()

    return render_template("view_students.html", students=students)


# ---------------- DELETE STUDENT ----------------
@admin_bp.route("/admin/delete-student/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    if session.get("role") != "admin":
        return redirect("/")

    db = get_db()
    cur = db.cursor()

    # Delete related data first
    cur.execute("DELETE FROM answers WHERE student_id=?", (student_id,))
    cur.execute("DELETE FROM results WHERE student_id=?", (student_id,))
    cur.execute("DELETE FROM users WHERE id=? AND role='student'", (student_id,))

    db.commit()
    db.close()

    return redirect("/admin/students")
