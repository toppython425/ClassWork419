for number in range(1, 11):
    if number == 5 or number == 6:
        continue

    print(number)
print()

# print(1)
# print(2)
# print(3)
# print("...")
# print(10)

count = 1
while count <= 10:
    if count == 5 or count == 6:
        count += 1
        continue
    print(count)
    count += 1

for number in range(5):
    print(number)
print()
