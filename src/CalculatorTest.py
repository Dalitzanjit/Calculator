import unittest
from calculator import Calculator, addition, subtraction
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.addition(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtraction(2, 2), 0)
        self.assertEqual(calculator.result, 0)


if __name__ == '_main_':
    unittest.main()