import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# проблема - данные подтягиваются при помощи JS
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('div', class_='dynamic-content')

# решение - использовать selenium
driver = webdriver.Chrome()
driver.get("https://example.com")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
