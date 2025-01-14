# numbers = [10, 20, 30, 40]
# for num in numbers:
#     if num % 20 == 0:
#         numbers.remove(num)
# print(numbers)

# numbers = [10, 20, 30, 40]
# for num in numbers[:]:
#     if num % 20 == 0:
#         numbers.remove(num)
# print(numbers)


# def bubble_sort(lst):
#     n = len(lst)
#     while True:  # Ошибка: Условие выхода из цикла отсутствует
#         for i in range(n - 1):
#             if lst[i] > lst[i + 1]:
#                 lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     return lst
#
#
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(numbers))

# def bubble_sort(lst):
#     lst_len = len(lst)
#     for i in range(lst_len - 1):
#         for j in range(lst_len - 1 - i):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
#
#
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(numbers))

# numbers = [10, 20, 30, 40]
# target = 30
# for num in numbers:
#     if num == target:
#         print('Элемент найден!')
#         break
# else:
#     print('Элемент не найден')


def linear_search(lst, target):
    for num in lst:
        if num == target:
            return 'Элемент найден'
    return 'Элемент не найден'


numbers = [10, 20, 30, 40]
my_target = 50
print(linear_search(numbers, my_target))
