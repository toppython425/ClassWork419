# my_list = [1, 2.5, "Python", True, False]
# print(my_list)
#
# fruits = []
# fruits.append('apple')
# fruits.append('banana')
# fruits.append('cherry')
# print(fruits)
#
# other_fruits = ['elderberry', 'blackberry']
# # fruits.extend(['elderberry', 'blackberry'])
# fruits.extend(other_fruits)
# print(fruits)
# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
# nums_list = [1, 3, 4, 8, 2, 55, 11, 8]

# fruits_list.remove('banana')
# nums_list.remove(8)
# print(fruits_list)
# print(nums_list)

# item_to_remove = input('Введите элемент для удаления: ')
# if item_to_remove in fruits_list:
#     fruits_list.remove(item_to_remove)
# else:
#     print(f'Элемента {item_to_remove} нет в списке!')
# print(fruits_list)

# item_to_remove = input('Введите элемент для удаления: ')
# try:
#     fruits_list.remove(item_to_remove)
# except ValueError:
#     print(f"Элемента {item_to_remove} нет в списке")
# else:
#     print(f"Элемент {item_to_remove} успешно удален")
# finally:
#     print(fruits_list)

# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
# nums_list = [1, 3, 4, 8, 2, 55, 11, 8]
#
# popped_fruit = fruits_list.pop()
# popped_num = nums_list.pop()
#
# print(fruits_list, popped_fruit)
# print(nums_list, popped_num)
#
# popped_fruit = fruits_list.pop(2)
# popped_num = nums_list.pop(3)
#
# print(fruits_list, popped_fruit)
# print(nums_list, popped_num)

# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
# nums_list = [1, 3, 4, 8, 2, 55, 11, 8]

# index_to_pop = int(input("Укажите индекс элемента для удаления: "))
# if index_to_pop > len(fruits_list) - 1:
#     print(f"Максимальный индекс списка {len(fruits_list) - 1}")
# elif index_to_pop < -len(fruits_list):
#     print(f"Минимальный индекс списка {-len(fruits_list)}")
# else:
#     popped_fruit = fruits_list.pop(index_to_pop)
#     print(popped_fruit)
# print(fruits_list)

# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
#
# index_to_pop = int(input("Укажите индекс элемента для удаления: "))
# try:
#     popped_fruit = fruits_list.pop(index_to_pop)
# except IndexError:
#     print(f"Максимальный индекс списка {len(fruits_list) - 1}")
#     print(f"Минимальный индекс списка {-len(fruits_list)}")
# else:
#     print(popped_fruit)
# finally:
#     print(fruits_list)

# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
# nums_list = [1, 3, 4, 8, 2, 55, 11, 8]
#
# fruits_list.sort()
# nums_list.sort()
#
# print(fruits_list)
# print(nums_list)
#
# fruits_list.sort(reverse=True)
# nums_list.sort(reverse=True)
#
# print(fruits_list)
# print(nums_list)
#
# fruits_list = ['banana', 'cherry', 'apple', 'blackberry', 'banana', 'elderberry']
# nums_list = [1, 3, 4, 8, 2, 55, 11, 8]
#
# fruits_list.reverse()
# nums_list.reverse()
# print(fruits_list)
# print(nums_list)

fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
#                 0         1         2          3           4           5
#                -6        -5        -4         -3          -2          -1
print(fruits_list[3])
my_fruit = fruits_list[3]
print(my_fruit)

fruits_list[3] = 'peach'
print(fruits_list)
