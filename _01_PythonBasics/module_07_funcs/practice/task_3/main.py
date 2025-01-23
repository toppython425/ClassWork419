from string_utils import reverse_string, count_vowels, is_palindrome

while True:
    print('\nДоступные операции: 1 - reverse, 2 - count vowels, 3 - is_palindrome, 0 - exit')
    command = input("Введите операцию").strip().lower()

    if command == '0':
        print('Выход из программы.')
        break

    text_input = input('Введите текст на английском языке: ').strip()
    if command == '1':
        print(f'Перевернутая строка: {reverse_string(text_input)}')
    elif command == '2':
        print(f'Количество гласных: {count_vowels(text_input)}')
    elif command == '3':
        if is_palindrome(text_input):
            print('Строка является палиндромом')
        else:
            print('Строка не является палиндромом')
    else:
        print('Неизвестная команда попробуйте снова')
