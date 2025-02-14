from datetime import datetime, timedelta

# Текущая дата и время
now = datetime.now()
print(now)

# Создание объекта datetime с конкретными значениями
custom_datetime = datetime(2023, 5, 15, 14, 13, 45)
print(custom_datetime)
print()

# Разница в 5 дней
delta = timedelta(days=5)
print(delta)

# Арифметика с датами
today = datetime.today()
future_day = today + timedelta(days=10)
print(future_day)
