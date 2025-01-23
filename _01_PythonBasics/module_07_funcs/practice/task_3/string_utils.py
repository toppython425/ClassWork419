def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels_counter = 0
    vowels = 'aeiouAEIOU'
    for symbol in text:
        if symbol in vowels:
            vowels_counter += 1
    return vowels_counter

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]
