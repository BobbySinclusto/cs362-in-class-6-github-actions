import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, calculator.add(3, 2))

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 4), 16)

    def test_divide(self):
        self.assertEqual(calculator.divide(5, 5), 1)


if __name__ == '__main__':
    unittest.main()
