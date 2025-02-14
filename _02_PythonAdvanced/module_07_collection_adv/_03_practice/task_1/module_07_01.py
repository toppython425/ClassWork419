from collections import deque


class TaskQueue:

    def __init__(self, max_length):
        self.queue = deque(maxlen=max_length)

    def add_task(self, task):
        self.queue.append(task)

    def add_left_task(self, task):
        self.queue.appendleft(task)

    def get_tasks(self):
        return list(self.queue)


task_queue = TaskQueue(4)

task_queue.add_task('task1')
task_queue.add_task('task2')
task_queue.add_task('task3')
task_queue.add_task('task4')
print(task_queue.get_tasks())
task_queue.add_task('task5')
print(task_queue.get_tasks())
task_queue.add_left_task('task1')
print(task_queue.get_tasks())
