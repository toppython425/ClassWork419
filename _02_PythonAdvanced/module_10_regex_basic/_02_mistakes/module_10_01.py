import re

# text = "Сегодня 25 апреля 2023 года."
# pattern = r'\d'
# matches = re.findall(pattern, text)
# print(matches)

text = "Сегодня 25 апреля 2023 года."
pattern = r'\d+'
matches = re.findall(pattern, text)
print(matches)