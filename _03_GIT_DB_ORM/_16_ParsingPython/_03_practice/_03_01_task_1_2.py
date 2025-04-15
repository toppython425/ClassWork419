import requests
from bs4 import BeautifulSoup


def get_paragraphs(url):
    """
    Получение всех параграфов с указанной страницы
    :param url: адрес ресурса
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    result = []
    for p in soup.find_all('p'):
        text = p.get_text().strip()
        if text:
            result.append(text)
    return result


if __name__ == "__main__":
    url = "https://spb.top-academy.ru"
    paragraphs = get_paragraphs(url)

    if paragraphs:
        print(paragraphs[:100])
    else:
        print("Не удалось получить параграфы со страницы")
