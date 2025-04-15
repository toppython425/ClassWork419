import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# проблема - Старый парсер
# После изменений на сайте класс стал 'new-price-class'
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find('span', class_='product-price').text


# Решение 1 - Использовать более устойчивые селекторы (например, data-атрибуты).
#         2 - Реализовать систему оповещений о сбоях:


def send_alert():
    pass


try:
    price = soup.find('span', {'data-testid': 'price'}).text
except AttributeError:
    send_alert("Структура страницы изменилась!")
