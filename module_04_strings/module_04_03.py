# greeting = "Hello, world!"
# first_letter = greeting[0]
# print(first_letter)
# sub_string = greeting[0:7]
# print(sub_string)
# last_letter = greeting[-1]
# print(last_letter)
#
# length = len(greeting)
# print(length)
#
# for char in greeting:
#     print(char)

# greeting = "Hello, world!"
# char_index = 0
# while greeting:
#     print(greeting[char_index])
#     char_index += 1
#     if char_index == len(greeting):
#         break

greeting = "Hello, world!"
for i in range(len(greeting)):
    print(f'Символ на индексе {i}: {greeting[i]}')