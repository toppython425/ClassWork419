import sqlite3

students = [
    ("Иван Иванов", 20, "Математика"),
    ("Анна Смирнова", 22, "Физика"),
    ("Петр Петров", 23, "Химия"),
    ("Екатерина Соколова", 21, "Биология")
]

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/students.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    );
    """)
    try:
        for student in students:
            cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", student)
    except sqlite3.Error as err:
        print(err)
    else:
        conn.commit()
    finally:
        conn.close()
