with open(r'files/Sheperd.jpg', 'rb') as file:
    data = file.read()
    print(f'Прочитано {len(data)} байт')
