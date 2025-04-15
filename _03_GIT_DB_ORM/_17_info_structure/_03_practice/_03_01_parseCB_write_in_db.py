import requests
from bs4 import BeautifulSoup


def parse_currency_rates():
    url = "https://www.cbr.ru/currency_base/daily/"

    try:
        response = requests.get(url=url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'data'})

        rates = {}
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 5:
                currency_code = cols[1].text.strip()
                if currency_code in ["USD", "EUR", "CNY"]:
                    unit = int(cols[2].text.strip())
                    value = float(cols[4].text.replace(',', '.'))
                    rates[currency_code] = {
                        'value': value,
                        'unit': unit
                    }
        return rates

    except requests.exceptions.RequestException as ex:
        print(f'Ошибка при запросе: {ex}')
        return None


if __name__ == '__main__':
    result = parse_currency_rates()
    if result:
        print('Актуальные курсы валют:')
        for currency, data in result.items():
            print(f'{currency}: {data['value']} руб. за {data['unit']} ед.')
    else:
        print(f"Не удалось получить данные")
