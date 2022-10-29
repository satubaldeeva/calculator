import unittest
import sys


from Calculator import *
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QMainWindow, QApplication
from operator import add, sub, mul, truediv
from design import Ui_MainWindow
import Calculator


was_checked = False


def the_button_was_toggled():
    global was_checked
    was_checked = True
    return was_checked


# python -m unittest -v TestCalculator.py
app = QApplication(sys.argv)


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.form = Calculator.Calculator()

    def test_result_add(self):
        self.assertEqual(result("+", 2, 8), 10)

    def test_result_div_zero(self):
        self.assertEqual(result("/", 10, 2), 5)
        self.assertRaises(ZeroDivisionError, lambda: result("/", 10, 0))

    def test_result_div(self):
        self.assertEqual(result("/", 10, 2), 5)
        self.assertRaises(ArithmeticError, lambda: result("/", 10, 0.00000000001))

    def test_result_sub(self):
        self.assertEqual(result("-", 2, 0), 2)
        self.assertEqual(str(result("--", 2, 0)), "None")

    def test_result_mul(self):
        self.assertEqual(result("*", 2, 6), 12)
        with self.assertRaises(Exception):
            result("+", "sd", 23)

    def test_Buttons(self):
        # Btn_0
        self.form.ui.btn_0.setCheckable(True)
        print(self.form.ui.btn_0.objectName())
        self.form.ui.btn_0.click()
        self.assertEqual(self.form.ui.l_e.text(), "0")
        #Btn_1
        self.form.ui.btn_1.setCheckable(True)
        print(self.form.ui.btn_1.objectName())
        self.form.ui.btn_1.click()
        self.assertEqual(self.form.ui.l_e.text(), "1")
        self.form.ui.l_e.setText("0")

        # Btn_2

        print(self.form.ui.btn_2.objectName())
        self.form.ui.btn_2.click()
        self.assertEqual(self.form.ui.l_e.text(), "2")
        self.form.ui.l_e.setText("0")

        #Btn_3
        print(self.form.ui.btn_3.objectName())
        self.form.ui.btn_3.click()
        self.assertEqual(self.form.ui.l_e.text(), "3")
        self.form.ui.btn_ce.click()

        # Btn_4
        print(self.form.ui.btn_4.objectName())
        self.form.ui.btn_4.click()
        self.assertEqual(self.form.ui.l_e.text(), "4")
        self.form.ui.l_e.setText("0")
        # Btn_5
        print(self.form.ui.btn_5.objectName())
        self.form.ui.btn_5.click()
        self.assertEqual(self.form.ui.l_e.text(), "5")
        self.form.ui.l_e.setText("0")
        #Btn_6

        print(self.form.ui.btn_6.objectName())
        self.form.ui.btn_6.click()
        self.assertEqual(self.form.ui.l_e.text(), "6")
        self.form.ui.l_e.setText("0")


        # Btn_7
        print(self.form.ui.btn_7.objectName())
        self.form.ui.btn_7.click()
        self.assertEqual(self.form.ui.l_e.text(), "7")
        self.form.ui.l_e.setText("0")

        # Btn_8
        print(self.form.ui.btn_8.objectName())
        self.form.ui.btn_8.click()
        self.assertEqual(self.form.ui.l_e.text(), "8")
        self.form.ui.l_e.setText("0")

        # Btn_9
        print(self.form.ui.btn_9.objectName())
        self.form.ui.btn_9.click()
        self.assertEqual(self.form.ui.l_e.text(), "9")
        self.form.ui.l_e.setText("0")

        # Btn_clear_all
        self.form.ui.l_e.setText("1")
        self.form.ui.lbl_temp.setText("1")
        print(self.form.ui.btn_ce.objectName())
        self.form.ui.btn_ce.click()
        self.assertEqual(self.form.ui.l_e.text(), "0")
        self.assertEqual(self.form.ui.lbl_temp.text(), "")

        # Btn_clear_entry
        print(self.form.ui.btn_c.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_c.click()
        self.assertEqual(self.form.ui.l_e.text(), "0")

        #Point adding
        print(self.form.ui.btn_point.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_point.click()
        self.assertEqual(self.form.ui.l_e.text(), "1.")


        #Div
        print(self.form.ui.btn_div.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_div.click()
        self.assertEqual(self.form.ui.lbl_temp.text(), "1 / ")
        self.form.ui.btn_ce.click()

        # Plus
        print(self.form.ui.btn_div.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_plus.click()
        self.assertEqual(self.form.ui.lbl_temp.text(), "1 + ")
        self.form.ui.btn_ce.click()

        # Min
        print(self.form.ui.btn_div.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_min.click()
        self.assertEqual(self.form.ui.lbl_temp.text(), "1 - ")
        self.form.ui.btn_ce.click()

        # Multy
        print(self.form.ui.btn_div.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_multy.click()
        self.assertEqual(self.form.ui.lbl_temp.text(), "1 * ")
        self.form.ui.btn_ce.click()

       #Result
        print(self.form.ui.btn_res.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_div.click()
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_res.click()
        self.assertEqual(self.form.ui.l_e.text(), "1")

    #Plus/neg
        print(self.form.ui.btn_plus_min.objectName())
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_plus_min.click()
        self.assertEqual(self.form.ui.l_e.text(), "-1")

        # backspace
        print(self.form.ui.btn_backspace.objectName())
        self.form.ui.l_e.setText("10")
        self.form.ui.btn_backspace.click()
        self.assertEqual(self.form.ui.l_e.text(), "1")

        self.form.ui.l_e.setText("-1")
        self.form.ui.btn_backspace.click()
        self.assertEqual(self.form.ui.l_e.text(), "0")

        #exception
        self.form.ui.l_e.setText("0")
        self.form.ui.btn_div.click()
        self.form.ui.l_e.setText("1")
        self.form.ui.btn_res.click()
        self.assertEqual(self.form.ui.l_e.text(), "0")




if __name__ == "__main__":
    unittest.main()
