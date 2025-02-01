import unittest

division = lambda a, b: a / b


# class TestMath(unittest.TestCase):
#     def addition(self):
#         result = 2 + 2
#         self.assertEqual(result, 4)


class TestMath(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)
        # self.assertEqual(result, 5)

    def test_division(self):
        # self.assertRaises(ZeroDivisionError, division(1, 0))
        self.assertRaises(ZeroDivisionError, division, 1, 0)
        with self.assertRaises(ZeroDivisionError):
            division(1, 0)
