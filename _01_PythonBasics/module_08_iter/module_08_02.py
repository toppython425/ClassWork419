numbers_list = [1, 2, 3]
numbers_iterator = iter(numbers_list)

while True:
    try:
        print(next(numbers_iterator))
    except StopIteration:
        break
