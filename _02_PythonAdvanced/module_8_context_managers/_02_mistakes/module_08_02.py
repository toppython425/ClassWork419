# class OpenToRead:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.file, 'r')
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         pass  # завершаем метод, не закрыв файл


class OpenToRead:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.file, 'r')

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
