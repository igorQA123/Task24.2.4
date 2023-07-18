import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def test_multiplay(self):
        assert self.calc.multiplay(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self, 2, 2) == 1

