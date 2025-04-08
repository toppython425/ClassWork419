import json
import os

from dotenv import load_dotenv
import requests
from requests import exceptions


class WeatherAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru'
        }
        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            return {
                'city': city,
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }
        except exceptions.HTTPError as ex:
            if response.status_code == 404:
                print(f'Город {city} не найден.')
            else:
                print(f'Ошибка API: {ex}')
        except exceptions.Timeout:
            print('Сервер не ответил за 5 секунд')
        except exceptions.RequestException as ex:
            print(f'Ошибка подключения: {ex}')
        return None

    @classmethod
    def save_to_json(cls, data, filename='weather_data.json'):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        print(f'Данные сохранены в {filename}')


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    weather_app = WeatherAPI(API_KEY)
    city = input("Введите город: ")
    weather_data = weather_app.get_weather(city)

    if weather_data:
        print(f"\nПогода в {city}:")
        print(f"Температура: {weather_data['temp']}°C")
        print(f"Ощущается как: {weather_data['feels_like']}°C")
        print(f"Влажность: {weather_data['humidity']}%")

        WeatherAPI.save_to_json(weather_data)
    else:
        print("Не удалось получить данные о погоде.")
