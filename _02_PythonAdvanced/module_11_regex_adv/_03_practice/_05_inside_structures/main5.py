import re

text = "Пример: {внешняя {внутренняя}}, а также (скобки (внутри)). Также проверьте [вложенные [структуры]]."

pattern = re.compile(r'\{[^{}]*}|\([^()]*\)|\[[^\[\]]*]')
matches = re.findall(pattern, text)
print(matches)
