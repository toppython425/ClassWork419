from multiprocessing import Process, Queue


def power_numbers(numbers, exponent, result_queue):
    results = [num ** exponent for num in numbers]
    result_queue.put(results)


if __name__ == '__main__':
    numbers = list(range(1, 21))
    exponent = 2
    num_process = 4

    result_queue = Queue()

    chunk_size = len(numbers) // num_process
    processes = []

    for i in range(num_process):
        start_idx = i * chunk_size
        # end_idx = (i + 1) * chunk_size if i < num_process - 1 else len(numbers)
        if i < num_process - 1:
            end_idx = (i + 1) * chunk_size
        else:
            end_idx = len(numbers)

        chunk = numbers[start_idx: end_idx]

        process = Process(target=power_numbers, args=(chunk, exponent, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    all_results = []
    while not result_queue.empty():
        all_results.extend(result_queue.get())

    print(f"Результаты: {all_results}")
