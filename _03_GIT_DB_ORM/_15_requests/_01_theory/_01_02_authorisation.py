import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

headers = {
    'Authorisation': API_KEY
}

params = {
    'q': 'London',
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params=params,
    headers=headers
)

if response.status_code == 200:
    data = response.json()
    print(data)
    print(f'Погода в {data['name']}: {data['weather'][0]['description']}')
    print(f'Температура: {data['main']['temp']}°C')
else:
    print(f'Ошибка: {response.status_code}, {response.text}')


