import unittest
from calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 4)


if __name__ == '__main__':
    unittest.main()