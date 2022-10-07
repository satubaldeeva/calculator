import unittest
import sys
from Calculator import *
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QMainWindow, QApplication
from operator import add, sub, mul, truediv
from design import Ui_MainWindow

# python -m unittest -v TestCalculator.py


class TestCalculator(unittest.TestCase):

    def test_result_add(self):
        self.assertEqual(result("+", 2, 8), 10)

    def test_result_div(self):
        self.assertEqual(result("/",10, 2), 5)
        self.assertRaises(ZeroDivisionError, lambda: result("/",10, 0))
        # try:
        #     division(10, 0)
        # except ZeroDivisionError:
        #     print("111!")
        self.assertRaises(ArithmeticError, lambda: result("/", 10, 0.00000000001))

    def test_result_sub(self):
        self.assertEqual(result("-", 2, 0), 2)
        self.assertEqual(str(result("--", 2, 0)), "None")

    def test_result_mul(self):
        self.assertEqual(result("*", 2, 6), 12)
        with self.assertRaises(Exception):
            result("+","sd",23)


if __name__ == "__main__":
    unittest.main()
