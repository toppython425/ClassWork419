def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        return content
