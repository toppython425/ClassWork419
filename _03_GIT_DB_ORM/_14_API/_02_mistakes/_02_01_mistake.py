import requests

# response = requests.get("https://api.example.com/data")
# data = response.json()  # Ошибка, если response.status_code != 200

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
except requests.exceptions.ConnectionError as ex:
    print(ex)
else:
    data = response.json()
