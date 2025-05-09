from code import calculator  # import your calculator code
import unittest              # import Python's unittest module

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(0, 7), -7)

if __name__ == '__main__':
    unittest.main()
