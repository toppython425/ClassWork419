class FileWriter:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self

    def write(self, text):
        self.file.write(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Ошибка: {exc_type.__name__} - {exc_val}')
        self.file.close()
        return True


with FileWriter(r'files\output.txt') as writer:
    writer.write('Hello, world!\n')
    raise Exception("Ошибка при записи!")
