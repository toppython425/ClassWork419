import threading
import queue


class ThreadPool:
    def __init__(self, max_threads):
        self.max_threads = max_threads
        self.task_queue = queue.Queue()
        self.running_threads = 0

    def add_task(self, task_func, *args):
        self.task_queue.put((task_func, args))
        self._try_run_task()

    def _worker(self):
        task_func, args = self.task_queue.get()
        task_func(*args)
        self.task_queue.task_done()

        # после завершения задачи уменьшаем количество работающих потоков
        with threading.Lock():
            self.running_threads -= 1

        # попробуем запустить следующую задачу, если есть свободные потоки
        self._try_run_task()

    def _try_run_task(self):
        # если количество работающих потоков меньше максимального, запускаем новый
        if self.running_threads < self.max_threads:
            with threading.Lock():
                self.running_threads += 1
            threading.Thread(target=self._worker).start()
