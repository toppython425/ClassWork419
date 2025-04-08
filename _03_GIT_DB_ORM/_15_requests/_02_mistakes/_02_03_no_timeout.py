import requests

# Без timeout программа может зависнуть
requests.get("https://api.example.com/slow-endpoint")  # Ждет вечно...

# Через 5 сек. выбросится исключение Timeout
requests.get("https://api.example.com/slow-endpoint", timeout=5)
