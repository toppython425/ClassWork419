from math import sqrt
# from math import calculate


def greet(name):
    print(f'Hello, {name}')


greet("Alice")


def add(a, b=0):
    return a + b


result = add(5)
print(result)

my_sqrt = 'Not a func'
print(sqrt(16))
