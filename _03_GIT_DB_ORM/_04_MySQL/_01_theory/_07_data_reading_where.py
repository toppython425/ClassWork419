import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'data_bases/students.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE course = ?", ("Математика",))
        math_studs = cursor.fetchall()

    except sqlite3.Error as err:
        print(err)
    else:
        print(math_studs)
    finally:
        conn.close()
