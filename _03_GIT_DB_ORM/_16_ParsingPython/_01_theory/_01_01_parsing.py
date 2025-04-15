import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/articles/'
url_article = 'https://habr.com/ru/companies/pgk/articles/897658/'

try:
    response = requests.get(url_article)
except requests.RequestException as ex:
    print(ex)
else:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # Находит первый тег с заголовками первого уровня <h1>
    title = soup.find('h1')
    # print(title)
    # Все теги параграфов <p>
    all_paragraphs = soup.find_all('p')
    # print(all_paragraphs)
    # Находит элемент div с классом "tm-article-body"
    article_content = soup.find('div', class_='tm-article-body')
    # print(article_content)

    author_link = soup.find('a', {"href": "ru/users/username/"})
    # print(author_link)

    title1 = soup.find("h1", class_='tm-title').text.strip()
    content = soup.find("div", class_="tm-article-body").text.strip()
    print(f'Заголовок: {title1}\n\nТекст: {content[:200]}...')
