import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc=Calculator()
        result=calc.add(3,8)
        self.assertEqual(result,11)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(17,2)
        self.assertEqual(result, 34)
        
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

if __name__=="__main__":
    unittest.main