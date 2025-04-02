import sqlite3

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
        # cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        #                ("Иван Иванов", 20, "Математика"))
        # cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        #                ("Анна Смирнова", 22, "Физика"))
        cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                       ("Петр Петров", 23, "Химия"))
        cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                       ("Екатерина Соколова", 21, "Биология"))
    except sqlite3.Error as err:
        print(err)
    else:
        conn.commit()
    finally:
        conn.close()

