import sqlite3

db = sqlite3.connect("online_exam.db")
cur = db.cursor()

# ---------------- ADD SUBJECTS SAFELY ----------------
new_subjects = ["C", "C++", "C#"]

for s in new_subjects:
    cur.execute(
        "INSERT OR IGNORE INTO subjects (name) VALUES (?)",
        (s,)
    )

# Fetch subject IDs
cur.execute("SELECT id, name FROM subjects")
subject_map = {row[1]: row[0] for row in cur.fetchall()}

# ---------------- C QUESTIONS (10) ----------------
c_questions = [
    (subject_map["C"], "C is a ___ language?", "Low level", "High level", "Scripting", "Markup", "a"),
    (subject_map["C"], "Who developed C?", "Dennis Ritchie", "Bjarne", "Guido", "James", "a"),
    (subject_map["C"], "C file extension?", ".cpp", ".java", ".c", ".cs", "c"),
    (subject_map["C"], "Which header is standard?", "stdio.h", "input.h", "system.h", "console.h", "a"),
    (subject_map["C"], "Which symbol ends statement?", ":", ";", ".", ",", "b"),
    (subject_map["C"], "Which loop is valid?", "if", "case", "for", "switch", "c"),
    (subject_map["C"], "Which operator gives address?", "*", "&", "%", "#", "b"),
    (subject_map["C"], "Output function?", "print()", "printf()", "cout", "write()", "b"),
    (subject_map["C"], "Which is NOT datatype?", "int", "float", "real", "char", "c"),
    (subject_map["C"], "Exit loop keyword?", "stop", "exit", "break", "end", "c")
]

# ---------------- C++ QUESTIONS (10) ----------------
cpp_questions = [
    (subject_map["C++"], "C++ is extension of?", "Java", "Python", "C", "C#", "c"),
    (subject_map["C++"], "Who developed C++?", "Dennis", "Bjarne Stroustrup", "Guido", "James", "b"),
    (subject_map["C++"], "OOP feature?", "Procedure", "Class", "Loop", "Array", "b"),
    (subject_map["C++"], "Object creation keyword?", "new", "this", "malloc", "create", "a"),
    (subject_map["C++"], "Scope resolution operator?", "::", ":", ".", "->", "a"),
    (subject_map["C++"], "Input-output header?", "stdio.h", "iostream", "io.h", "stream.h", "b"),
    (subject_map["C++"], "Supports polymorphism?", "Overloading", "Pointer", "Array", "Loop", "a"),
    (subject_map["C++"], "NOT OOP principle?", "Inheritance", "Encapsulation", "Compilation", "Abstraction", "c"),
    (subject_map["C++"], "Statement ends with?", ":", ";", ".", ",", "b"),
    (subject_map["C++"], "Exit loop keyword?", "break", "stop", "exit", "return", "a")
]

# ---------------- C# QUESTIONS (10) ----------------
csharp_questions = [
    (subject_map["C#"], "C# is developed by?", "Google", "Apple", "Microsoft", "IBM", "c"),
    (subject_map["C#"], "C# runs on?", "JVM", ".NET", "Python VM", "Node", "b"),
    (subject_map["C#"], "Class keyword?", "class", "define", "struct", "object", "a"),
    (subject_map["C#"], "Main method name?", "start()", "run()", "Main()", "init()", "c"),
    (subject_map["C#"], "Value type?", "String", "Array", "Struct", "Class", "c"),
    (subject_map["C#"], "Create object keyword?", "new", "this", "create", "alloc", "a"),
    (subject_map["C#"], "NOT access modifier?", "public", "private", "protected", "global", "d"),
    (subject_map["C#"], "LINQ supported by?", "C", "C++", "C#", "Java", "c"),
    (subject_map["C#"], "Statement ends with?", ":", ";", ".", ",", "b"),
    (subject_map["C#"], "Exit loop keyword?", "break", "exit", "stop", "end", "a")
]

# Insert questions
for q in c_questions + cpp_questions + csharp_questions:
    cur.execute("""
        INSERT INTO questions
        (subject_id, question, a, b, c, d, correct)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, q)

db.commit()
db.close()

print("✅ Added C, C++, C# (10 questions each) without affecting Python & Java")
