import re

my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии,
21.04.2024 - Гран При Китая;
05.05.2024 - Гран При Майами."""

pattern = re.compile(r'[,;:\n]+')
my_str_list = re.split(pattern, my_str)
print(my_str_list)
new_list = []
