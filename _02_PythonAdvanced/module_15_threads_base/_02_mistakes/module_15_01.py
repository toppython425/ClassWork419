import threading

# counter = 0


# def increment():
#     global counter
#     for _ in range(100000):
#         counter += 1
#
#
# threads = [threading.Thread(target=increment) for _ in range(5)]
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print(f"Counter value: {counter}")  # Может вывести значение меньше 500000


counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment) for _ in range(5)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Counter value: {counter}")  # Может вывести значение меньше 500000

