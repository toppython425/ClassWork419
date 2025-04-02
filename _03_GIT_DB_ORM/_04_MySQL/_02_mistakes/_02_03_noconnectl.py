import sqlite3

conn = sqlite3.connect(r'data_bases/students.db')
cursor = conn.cursor()

conn.close()
rows = []


try:
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        print(row)
        rows.append(row)
except sqlite3.Error:
    print("Соединение с БД закрыто!")


print(rows)


