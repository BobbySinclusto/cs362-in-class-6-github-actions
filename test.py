import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 2), 5)
        self.assertEqual(calculator.add(234, 1), 235)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(4, 29), -25)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 4), 16)
        self.assertEqual(calculator.multiply(2, 54), 108)

    def test_divide(self):
        self.assertEqual(calculator.divide(5, 5), 1)
        self.assertEqual(calculator.divide(20, 5), 4)


if __name__ == '__main__':
    unittest.main()
