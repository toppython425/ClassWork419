import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/articles/803869/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url=url, headers=headers, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1', class_="tm-title").text.strip()
    content = soup.find('div', class_='tm-article-body').text.strip()

    print(f'Заголовок: {title}\n')
    print(f'Текст статьи (начало):\n{content[:300]}...')

except requests.exceptions.RequestException as ex:
    print(f'Ошибка при запросе: {ex}')
except AttributeError:
    print("Не удалось найти нужные элементы на странице.")
except Exception as ex:
    print(f'Ошибка: {ex}')
