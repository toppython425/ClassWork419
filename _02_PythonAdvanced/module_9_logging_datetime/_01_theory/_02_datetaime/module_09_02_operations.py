from datetime import datetime

# текущее время
print(datetime.now())

# форматирование даты и времени

now = datetime.now()
formatted_data = now.strftime('%Y-%m-%d >> %H:%M:%S')
print(formatted_data)
formatted_data = now.strftime('%d*%m*%Y >> %H:%M:%S')
print(formatted_data)


# Вычисление разницы между датами
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 2, 11)

delta = date2 - date1
print(delta.days)
print(delta)
print(type(delta))
