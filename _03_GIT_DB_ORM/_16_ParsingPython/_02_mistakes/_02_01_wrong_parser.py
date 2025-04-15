from bs4 import BeautifulSoup

# broken_html = r'https:\\www.example.com'
# soup = BeautifulSoup(broken_html, 'html.parser')
# print(soup.find('div'))

broken_html = r'https:\\www.example.com'
soup = BeautifulSoup(broken_html, 'lxml')
print(soup.find('div'))
