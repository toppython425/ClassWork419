import re

text = "Посетите https://example.com или http://test.org/page?query=value. Также проверьте ftp://files.example.org."
pattern = re.compile(r'https?://(?:www\.)?\w+\.\w+(?:/\S*)?')
matches = re.findall(pattern, text)
print(matches)
