import unittest

class TestExample(unittest.TestCase):

    def test_01_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_02_addition(self):
        self.assertNotEqual(2 + 2, 5)

    def test_03_divide(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
