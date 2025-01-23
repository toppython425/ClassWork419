word = "Hello"
# print(word[5])

string_index = 6
if len(word) > string_index:
    print(word[string_index])
else:
    print("Индекс вне диапазона!")


word = "Hello"
new_word = 'J' + word[1:]
print(new_word)

symbols_list = list(word)
symbols_list[0] = "J"
joined_symbols = "".join(symbols_list)

age = 25
# message = "I am " + age +" years old."
message = "I am " + str(age) +" years old."
print(message)