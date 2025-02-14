from collections import deque

# ограничение длины очереди
d = deque(maxlen=3)
print(d)

d.append(10)
d.append(5)
d.appendleft(3)
print(d)
print()
d.append(2)
print(d)
d.appendleft(7)
print(d)
print()

# перестановка элементов
d1 = deque([1, 2, 3, 4])
d1.rotate(2)
print(d1)
d1.rotate(-2)
print(d1)
