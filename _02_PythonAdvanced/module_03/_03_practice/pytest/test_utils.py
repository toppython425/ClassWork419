from utils import count_punct_marks


def test_empty_string(string_for_test):
    assert count_punct_marks(string_for_test[0]) == 0


def test_no_punctuation(string_for_test):
    assert count_punct_marks(string_for_test[1]) == 0


def test_single_punctuation(string_for_test):
    assert count_punct_marks(string_for_test[2]) == 1
    assert count_punct_marks(string_for_test[3]) == 1


def test_multiple_punctuation(string_for_test):
    assert count_punct_marks(string_for_test[4]) == 2


def test_all_punctuation(string_for_test):
    assert count_punct_marks(string_for_test[5]) == 7
