import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, calculator.add(3, 2))


if __name__ == '__main__':
    unittest.main()
