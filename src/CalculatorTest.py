import unittest
from calculator import Calculator, addition, subtraction
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(calculator.addition(1, 1), 2)

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtraction(2, 2), 0)

    def test_results_property(self):
        calculator = Calculator()
        calculator.addition(2, 1)
        self.assertEqual(calculator.result, 0)


if __name__ == '_main_':
    unittest.main()
