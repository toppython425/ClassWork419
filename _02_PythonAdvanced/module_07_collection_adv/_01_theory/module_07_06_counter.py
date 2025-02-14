from collections import Counter

c1 = Counter(a=2, b=1)
print(c1)
c2 = Counter(a=1, b=2)
print(c1 + c2)
print(c1 - c2)
print(c1 & c2)
print(c1 | c2)
