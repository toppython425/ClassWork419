# event1_guests = ['Alice', 'Bob', 'Charlie', 'David']
# event2_guests = ['Charlie', 'Eve', 'Alice', 'Frank']
#
# event1_set = set(event1_guests)
# event2_set = set(event2_guests)
#
# both_events = event1_set & event2_set
# # both_events = event1_set.union(event2_set)
# only_event1 = event1_set - event2_set
# # only_event1 = event1_set.difference(event2_set)
# only_event2 = event2_set - event1_set
# # only_event2 = event2_set.difference(event1_set)
#
# print(f'Оба {both_events}')
# print(f'Только первое {only_event1}')
# print(f'Только второе {only_event2}')

text1 = input("Введите первый текст: ")
text2 = input("Введите второй текст: ")

# text_list_1 = text1.split()
# text_list_2 = text2.split()
#
# set1 = set(text_list_1)
# set2 = set(text_list_2)

set1 = set(text1.split())
set2 = set(text2.split())

common_words = set1 & set2
unique_to_text1 = set1 - set2
unique_to_text2 = set2 - set1

print(f"Слова в обоих текстах: {common_words}")
print(f"Слова только в первом тексте: {unique_to_text1}")
print(f"Слова только во втором тексте: {unique_to_text2}")
