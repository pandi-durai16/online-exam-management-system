from flask import Blueprint, render_template, request, redirect, session
from utils.db import get_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        db = get_db()
        cur = db.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        )
        user = cur.fetchone()

        if user:
            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "admin":
                return redirect("/admin")
            return redirect("/student")

        return render_template("login.html", error="Invalid login")

    return render_template("login.html")
