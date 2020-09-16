import pytest
from steps.oop_calculator import Calculator 

calculator = Calculator()

class Test_Calculator:
    def test_divide_function(self):
        result = calculator.divide(4,2) 
        assert result == 2

    def test_multiply_function(self):
        result = calculator.multiply(3,2)
        assert result == 6

    def test_subtract_function(self):
        result = calculator.subtract(4,3)
        assert result == 1

    def test_add_function(self):
        result = calculator.add(3,2)
        assert result == 5