import pytest

add = lambda a, b: a + b
product = lambda a, b: a * b
division = lambda a, b: a / b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_product():
    assert product(3, 5) == 15


def test_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
