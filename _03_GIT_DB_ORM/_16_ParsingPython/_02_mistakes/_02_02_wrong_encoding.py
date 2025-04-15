import requests
from bs4 import BeautifulSoup

# проблема не указана кодировка
# response = requests.get("https://site.com")
# soup = BeautifulSoup(response.text, "lxml")

# решение - указать кодировку
response = requests.get("https://site.com")
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "lxml")
