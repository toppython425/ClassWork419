# Список заказов
from module_02.module_02_01 import count

orders = ["Кофе", "Чай", "Пирожное", "Сэндвич"]
orders_iterator = iter(orders)

# while True:
#     try:
#         print(next(numbers_iterator))
#     except StopIteration:
#         break

while True:
    try:
        order = next(orders_iterator)
        print(f'Обрабатывается заказ: {order}')
    except StopIteration:
        print('Все заказы обработаны.')
        break

# Список шагов рецепта
recipe_steps = [
    "Нагрейте сковороду",
    "Добавьте масло",
    "Положите нарезанные овощи",
    "Обжарьте до готовности",
    "Посыпьте специями и подавайте"
]

recipe_steps_iterator = iter(recipe_steps)
steps_counter = 1
while True:
    try:
        step = next(recipe_steps_iterator)
        print(f'Шаг {steps_counter}: {step}')
        steps_counter += 1
    except StopIteration:
        print("Рецепт завершен.")
        break
