from collections import defaultdict


def group_products_by_category(items: list) -> defaultdict:
    grouped = defaultdict(list)

    for category, product in items:
        grouped[category].append(product)

    return grouped


items_list = [
    ("Фрукты", "Яблоко"),
    ("Овощи", "Морковь"),
    ("Фрукты", "Банан"),
    ("Молочные продукты", "Молоко"),
    ("Овощи", "Картофель")
]

result = group_products_by_category(items_list)
print(result)
# print(dict(result))
for key, value in result.items():
    print(f'Категория: {key}. Продукты: {', '.join(value)}')
