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
        if self.file:
            self.file.close()


with FileWriter(r'files\output.txt') as writer:
    writer.write('Hello, world!\n')
