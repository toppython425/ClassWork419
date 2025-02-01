import unittest


def divide(a, b):
    if b == 0:
        raise ValueError('На 0 делить нельзя')
    return a / b


class TestFuncs(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        # self.assertRaises(ValueError, divide, 10, 0)
        with self.assertRaises(ValueError):
            divide(10, 0)
