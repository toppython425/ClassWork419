import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/students.db')
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE students SET course = ? WHERE name = ?", ("Информатика", "Иван Иванов"))
        cursor.execute("SELECT * FROM students WHERE course = ?", ("Информатика",))
        informathic_studs = cursor.fetchall()
    except sqlite3.Error as err:
        print(err)
    else:
        print(informathic_studs)
        conn.commit()
    finally:
        conn.close()
