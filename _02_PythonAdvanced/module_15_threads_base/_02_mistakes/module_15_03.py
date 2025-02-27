import threading


# def worker():
#     print("Working...")
#
#
# thread = threading.Thread(target=worker)
# thread.join()
# thread.start()


def worker():
    print("Working...")


thread = threading.Thread(target=worker)
thread.start()
thread.join()
