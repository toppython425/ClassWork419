import requests

# API ждет JSON, но заголовок не указан
requests.post("https://api.example.com", data={"key": "value"})
# Сервер отвечает: 415 (т. к. данные ушли как form-data, а не JSON)


requests.post(
    "https://api.example.com",
    json={"key": "value"},
    headers={"Content-Type": "application/json"}  # Теперь сервер поймет данные
)
