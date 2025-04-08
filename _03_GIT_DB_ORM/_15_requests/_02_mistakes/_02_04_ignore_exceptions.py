import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

# response = requests.get("https://api.example.com/invalid-url")
# data = response.json()  # Ошибка, если response.status_code == 404


# response = requests.get("https://api.example.com/invalid-url")
# if response.status_code == 200:
#     data = response.json()
# else:
#     print(f"Ошибка {response.status_code}: {response.text}")


try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()
    data = response.json()
except HTTPError as http_err:
    print(f'HTTP ошибка: {http_err}')
except ConnectionError:
    print(f'Не удалось подключится к серверу')
except Timeout:
    print(f'Превышено время ожидания ответа от сервера')
except RequestException as err:
    print(f'Ошибка при выполнении запроса: {err}')
