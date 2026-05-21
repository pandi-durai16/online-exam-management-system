import sqlite3

db = sqlite3.connect("online_exam.db")
cur = db.cursor()

# ---------- PYTHON QUESTIONS ----------
python_questions = [
    (1, "Python is a ___ language?", "Low level", "High level", "Machine", "Assembly", "b"),
    (1, "Which keyword defines a function?", "func", "define", "def", "method", "c"),
    (1, "Which is immutable?", "List", "Set", "Tuple", "Dictionary", "c"),
    (1, "Which symbol is used for comments?", "//", "#", "/* */", "--", "b"),
    (1, "Which data type stores True/False?", "int", "bool", "str", "float", "b"),
    (1, "Which loop is used for sequences?", "while", "do-while", "for", "loop", "c"),
    (1, "Which keyword creates a class?", "function", "define", "class", "object", "c"),
    (1, "Which operator is used for power?", "^", "**", "//", "%", "b"),
    (1, "Which function gets user input?", "input()", "scan()", "read()", "get()", "a"),
    (1, "Which keyword stops a loop?", "stop", "exit", "break", "end", "c")
]

# ---------- JAVA QUESTIONS ----------
java_questions = [
    (2, "Java is a ___ language?", "Procedural", "Object Oriented", "Assembly", "Low level", "b"),
    (2, "Who invented Java?", "Dennis Ritchie", "James Gosling", "Guido", "Bjarne", "b"),
    (2, "Which keyword creates object?", "class", "new", "this", "create", "b"),
    (2, "Which method is entry point?", "main()", "start()", "run()", "init()", "a"),
    (2, "Which keyword is used to inherit?", "this", "super", "extends", "implements", "c"),
    (2, "Which is not OOP principle?", "Inheritance", "Encapsulation", "Compilation", "Polymorphism", "c"),
    (2, "Which data type stores decimal?", "int", "float", "boolean", "char", "b"),
    (2, "Which symbol ends statement?", ":", ";", ".", ",", "b"),
    (2, "Which package is default?", "java.io", "java.util", "java.lang", "java.net", "c"),
    (2, "Which keyword stops loop?", "break", "stop", "exit", "return", "a")
]

# Insert Python questions
for q in python_questions:
    cur.execute("""
        INSERT INTO questions
        (subject_id, question, a, b, c, d, correct)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, q)

# Insert Java questions
for q in java_questions:
    cur.execute("""
        INSERT INTO questions
        (subject_id, question, a, b, c, d, correct)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, q)

db.commit()
db.close()

print("✅ 10 Python + 10 Java questions inserted successfully!")
