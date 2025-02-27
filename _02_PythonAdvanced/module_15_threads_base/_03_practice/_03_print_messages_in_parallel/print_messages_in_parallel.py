import threading
import time


def upload_file(file_name, delay):
    print(f'Начало загрузки файла {file_name}...')
    time.sleep(delay)
    print(f'Файл {file_name} успешно загружен!')
    return file_name


def monitor_file_uploads():
    files = [('file1.txt', 6), ('file2.txt', 4), ('file3.txt', 8)]
    threads = []
    files_output = []

    for file, delay in files:
        thread = threading.Thread(target=upload_file, args=(file, delay))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        files_output.append(thread.join())


if __name__ == '__main__':
    print(monitor_file_uploads())