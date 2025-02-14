import re

my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии;
21.04.2024 - Гран При Китая."""

new_str = re.sub(r'[.]', '**', my_str)
new_str = re.sub(r'[:]', '-', new_str)
print(new_str)
