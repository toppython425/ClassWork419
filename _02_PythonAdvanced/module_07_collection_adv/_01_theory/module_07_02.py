from collections import deque

d = deque()
print(d)
# добавление
d.append(10)
d.append(5)
d.appendleft(3)
print(d)
print()

# удаление
print(d.pop())
print(d.popleft())
print(d)
print()

# индексация
d.append(5)
d.append(7)
d.appendleft(2)
print(d)
print(d[0])
print(d[1])
print(d[2])
# print(d[5])
