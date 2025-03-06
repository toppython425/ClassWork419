from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=100)


shm.close()
shm.unlink()