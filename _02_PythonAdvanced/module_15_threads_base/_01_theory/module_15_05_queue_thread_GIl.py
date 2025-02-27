import threading
import queue
import os


def process_file(q, result, lock):
    while not q.empty():
        file_path = q.get()
        try:
            if not os.path.exists(file_path):
                print(f'File not found: {file_path}')
                q.task_done()
                continue

            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                line_count = len(lines)

            with lock:
                result['total_lines'] += line_count
                result['file_results'][file_path] = line_count

            print(f'Processed {file_path}: {line_count} lines')

        except Exception as e:
            print(f'Error processing file {file_path}: {e}')

        finally:
            q.task_done()


def main():
    file_paths = [
        r'files/file1.txt',
        r'files/file2.txt',
        r'files/file3.txt',
    ]

    task_queue = queue.Queue()

    for path in file_paths:
        task_queue.put(path)

    result = {
        'total_lines': 0,
        'file_results': {}
    }

    result_lock = threading.Lock()

    num_threads = 3
    threads = [
        threading.Thread(target=process_file, args=(task_queue, result, result_lock)) for _ in range(num_threads)
    ]

    for thread in threads:
        thread.start()

    task_queue.join()

    print('\nResults:')
    for file_path, line_count in result['file_results'].items():
        print(f'{file_path}: {line_count} lines')
    print(f'Total lines: {result["total_lines"]}')
    print(result)


if __name__ == '__main__':
    main()

