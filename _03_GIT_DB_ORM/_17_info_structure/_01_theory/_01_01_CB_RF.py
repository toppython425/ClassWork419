import requests
from bs4 import BeautifulSoup


def parse_currency_rates():
    url = "https://www.cbr.ru/currency_base/daily/"

    try:
        # 1. Отправляем HTTP-запрос к странице
        response = requests.get(url=url)
        # 2. Создаем объект BeautifulSoup для анализа HTM
        soup = BeautifulSoup(response.text, 'html.parser')
        # 3. Находим таблицу с курсами валют
        table = soup.find('table', class_='data')
        # 4. Извлекаем все строки таблицы, кроме заголовка
        rows = table.find_all('tr')[1:]
        # 5. Создаем словарь для хранения результатов
        rates = {}
        # 6. Обрабатываем каждую строку таблицы
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                currency = cols[1].text.strip()
                # 7. Фильтруем только нужные валюты
                if currency in ['USD', 'EUR', 'BYN']:
                    # 8. Преобразуем значение курса в число
                    value = float(cols[4].text.replace(',', '.'))
                    rates[currency] = {'value': value}
        return rates
    except Exception as ex:
        print(ex)
        return {'error': 'Не удалось получить курсы'}
