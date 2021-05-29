import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, calculator.add(3, 2))
    
    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 1), 0)


if __name__ == '__main__':
    unittest.main()
