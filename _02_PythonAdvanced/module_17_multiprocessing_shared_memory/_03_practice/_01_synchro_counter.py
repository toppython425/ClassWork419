from multiprocessing import Process, shared_memory, Lock
import array


def worker(shm_name, lock):
    shm = shared_memory.SharedMemory(name=shm_name)
    counter = array.array('q', shm.buf)

    for _ in range(5):
        with lock:
            counter[0] += 1

    shm.close()


if __name__ == '__main__':
    shm = shared_memory.SharedMemory(create=True, size=array.array('q', [0]).itemsize)
    counter = array.array('q', shm.buf)
    counter[0] = 0

    lock = Lock()
    processes = [Process(target=worker, args=(shm.name, lock)) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    final_value = array.array('q', shm.buf)[0]
    print(f'Итоговое значение: {final_value}')

    shm.close()
    shm.unlink()
