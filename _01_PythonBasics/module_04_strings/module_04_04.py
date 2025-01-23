greeting = "   Hello, World!   "
formatted = greeting.strip()
print(formatted)
# "Hello, World!"
print(formatted.find('World'))
print(formatted.find(','))
print(formatted.upper())
print(formatted.lower())
print(formatted.title())
print(formatted.capitalize())
print(formatted.swapcase())

greeting = "Hello, World!"
new_greeting = greeting.replace("World", "Python").replace("Hello", "Hi")
print(greeting)
print(new_greeting)

text = "Python is fun"
words_list = text.split(" ")
print(words_list)

csv_line = "one, two, three"
items = csv_line.split(", ")
print(items)

joined = " ".join(words_list)
print(joined)
joined_items = ", ".join(items)
print(joined_items)

greeting = "Hello, World! Hello, World!"
print(greeting.count("o"))