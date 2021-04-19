import unittest

import calculator
from calculator import Calculator, Addition, subtraction
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition(self):
        self.assertEqual(calculator.addition(1, 1), 2)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(2, 2), 0)

    def test_results_property(self):
        import calculator
        calculator = Calculator()
        calculator.addition(2, 1)
        self.assertEqual(calculator.result, 0)

if __name__ == '_main_':
    unittest.main()
