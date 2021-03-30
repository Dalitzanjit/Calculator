from CsvReader import CsvReader

def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = a - b
    a = int(a)
    b = int(b)
    c = b - a
    return c

def mean(data):
 mean = data
 return mean

class Calculator:
    result = 0

    def subtract(self, a, b):
        self.result = subtraction (a, b)
        return self.result

class CSVStats(Calculator):
    data = []


def _init_(self, data_file):
    self.data = CsvReader(data_file)
    pass