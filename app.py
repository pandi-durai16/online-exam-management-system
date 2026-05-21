from flask import Flask
from modules.auth import auth_bp
from modules.exam import exam_bp
from modules.result import result_bp
from modules.admin import admin_bp
app = Flask(__name__)
app.secret_key = "exam_secret_key"
app.register_blueprint(auth_bp)
app.register_blueprint(exam_bp)
app.register_blueprint(result_bp)
app.register_blueprint(admin_bp)
if __name__ == "__main__":
    app.run(debug=True)
