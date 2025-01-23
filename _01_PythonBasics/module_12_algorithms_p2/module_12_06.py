from collections import deque

queue = deque([1, 2, 3])
# while queue:
#     print(queue[0])

while queue:
    print(queue.popleft())
print()

queue = deque([1, 2, 3])
# print(queue[-1])
# queue.popleft()
# print(queue[-1])

while queue:
    print(queue.popleft())
print()

