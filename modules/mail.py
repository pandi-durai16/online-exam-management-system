import smtplib
from email.mime.text import MIMEText

def send_mail(to_email, subject, message):
    msg = MIMEText(message)
    msg["From"] = "admin@examportal.com"
    msg["To"] = to_email
    msg["Subject"] = subject

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.send_message(msg)
    server.quit()
