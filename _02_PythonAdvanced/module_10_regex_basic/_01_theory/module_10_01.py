import re

# text = "Сегодня 25 апреля 2023 года."
#
# words = text.split()
# matches = list()
#
# for word in words:
#     if word.isdigit():
#         matches.append(word)
#
# print(matches)

text = "Сегодня 25 апреля 2023 года."
pattern = r'\d+'
matches = re.findall(pattern, text)
print(matches)

text = "Сегодня 25 04 2025 апреля 2023 года"
pattern = re.compile(r'\d+')
print(pattern)
matches = re.findall(pattern, text)
print(matches)

