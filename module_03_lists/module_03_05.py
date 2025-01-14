# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
# item_to_remove = input('Введите элемент для удаления: ')
#
# if item_to_remove in fruits_list:
#     fruits_list.remove(item_to_remove)
# else:
#     print(f'Элемента {item_to_remove} нет в списке!')
# print(fruits_list)
#
# item_to_remove = input('Введите элемент для удаления: ')
# try:
#     fruits_list.remove(item_to_remove)
# except ValueError:
#     print(f"Элемента {item_to_remove} нет в списке")
# else:
#     print(f"Элемент {item_to_remove} успешно удален")
# finally:
#     print(fruits_list)
#
# fruits_list = ['apple', 'banana', 'cherry', 'blackberry', 'banana', 'elderberry']
# nums_list = [1, 3, 4, 8, 2, 55, 11, 8]
#
# index_to_pop = int(input("Укажите индекс элемента для удаления: "))
# if index_to_pop > len(fruits_list) - 1:
#     print(f"Максимальный индекс списка {len(fruits_list) - 1}")
# elif index_to_pop < -len(fruits_list):
#     print(f"Минимальный индекс списка {-len(fruits_list)}")
# else:
#     popped_fruit = fruits_list.pop(index_to_pop)
#     print(popped_fruit)
# print(fruits_list)
#
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


# fruits_list = ['apple', 'banana', 'cherry']
# fruits_list_1 = fruits_list
# fruits_list_1.append('peach')
# print(fruits_list)
# print(fruits_list_1)
# fruits_list_1 = fruits_list[:]
# fruits_list_1.append('peach')
# print(fruits_list)
# print(fruits_list_1)
#
# fruits_list_2 = fruits_list.copy()
# fruits_list_2.append('pineapple')
# print(fruits_list)
# print(fruits_list_2)
#
# fruits_list_3 = list(fruits_list)
# fruits_list_3.append('blackberry')
# print(fruits_list)
# print(fruits_list_3)

# numbers = []
# while True:
#     numbers.append(1)

numbers = []
for i in range(100):
    numbers.append(i)
print(numbers)




