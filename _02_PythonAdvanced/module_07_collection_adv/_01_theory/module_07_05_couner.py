from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter_data = Counter(data)
print(counter_data)
print(counter_data['banana'])
print(counter_data['grape'])
print(counter_data.most_common(2))
counter_data.update(['apple', 'banana', 'grape'])
print(counter_data)

