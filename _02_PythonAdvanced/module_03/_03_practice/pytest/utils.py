import string


def count_punct_marks(some_string: str) -> int:
    total_count = 0
    symbols = string.punctuation
    for sym in symbols:
        total_count += some_string.count(sym)
    return total_count
