import re

# text = "Цена: $10.50"
#
# pattern = re.compile(r'\$\d+.')
# matches = re.findall(pattern, text)
# print(matches)

text = "Цена: $10.50"

pattern = re.compile(r'\$\d+\.\d+')
matches = re.findall(pattern, text)
print(matches)