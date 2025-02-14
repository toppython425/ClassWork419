from collections import Counter

text = "hello world"
c_text = Counter(text)
print(c_text)

words = ["python", "java", "python", "c++", "java", "python"]
c_words = Counter(words)
print(c_words.most_common(1))

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
c_numbers = Counter(numbers)
print(c_numbers)
