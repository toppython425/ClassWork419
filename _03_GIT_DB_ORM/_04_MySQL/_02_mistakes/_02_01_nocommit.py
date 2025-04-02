import sqlite3

students = [
    ("Иван Иванов", 20, "Математика"),
    ("Анна Смирнова", 22, "Физика"),
    ("Петр Петров", 23, "Химия"),
    ("Екатерина Соколова", 21, "Биология")
]

conn = sqlite3.connect(r'data_bases/students.db')
"""Если во всем уверены!"""
# conn.autocommit = True
cursor = conn.cursor()

try:
    cursor.execute("""DROP TABLE students""")
except sqlite3.Error as err:
    print(err)

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
);
""")

"""Неверно нет commit"""
# for student in students:
#     cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", student)
#
# conn.close()

for student in students:
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", student)

conn.commit()
conn.close()
