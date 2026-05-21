import sqlite3

db = sqlite3.connect("online_exam.db")
cur = db.cursor()

# Delete all exam-related data
cur.execute("DELETE FROM answers")
cur.execute("DELETE FROM results")

db.commit()
db.close()

print("✅ All exam attempts and scores deleted successfully!")
print("🔄 Exams are now reset and can be attempted again.")
