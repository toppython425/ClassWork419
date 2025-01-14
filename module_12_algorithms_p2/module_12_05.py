stack = [1, 2, 3, 4]

for num in stack:
    print(stack.pop())
print()

stack = [1, 2, 3, 4]
for item in stack[:]:
    print(stack.pop())
