import sqlite3

conn = sqlite3.connect(r'data_bases/students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students;")
"""Не желательно для очень объемных таблиц"""
# rows = cursor.fetchall()
# print(rows)

"""Либо задаем количество записей"""
# rows = cursor.fetchmany(3)
# print(rows)

"""Либо обрабатываем по 1й"""
rows = []
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)
    rows.append(row)

print(rows)

conn.close()
