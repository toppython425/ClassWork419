def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return f'Элемент найден! Индекс элемента {index}'
    return "Элемент не найден"


# def linear_search_alt(lst, target):
#     value_index = 0
#     for value in lst:
#         if value == target:
#             return f'Элемент найден! Индекс элемента {value_index}'
#         value_index += 1
#     return "Элемент не найден"


numbers = [10, 20, 30, 40, 50]
print(linear_search(numbers, 30))
# print(linear_search_alt(numbers, 30))
print(linear_search(numbers, 60))
