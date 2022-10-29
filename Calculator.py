import sys
from typing import Union, Optional
from PySide6.QtWidgets import QMainWindow, QApplication
from operator import add, sub, mul, truediv

from design import Ui_MainWindow

operations = {
    '+': add,
    '-': sub,
    '/': truediv,
    '*': mul,
}


def result(sign: str, x: Union[int, float], y: Union[int, float]):
    if sign == "+":
        return x + y
    if sign == "-":
        return x - y
    if sign == "*":
        return x * y
    if sign == "/":
        try:
            res = x / y
            if int(y) <= 0.00000001:
                raise ArithmeticError
            else:
                return res
        except ZeroDivisionError:
            raise ZeroDivisionError('Division by zero!')
        except ArithmeticError:
            raise ArithmeticError('Divisor less than 10^(-8)!!')
    # return "None"


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max_len = self.ui.l_e.maxLength()

        # digits

        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        # actions
        self.ui.btn_ce.clicked.connect(self.clear_all)
        self.ui.btn_c.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)

        # MATH
        self.ui.btn_res.clicked.connect(self.calculate)
        self.ui.btn_plus_min.clicked.connect(self.negate)
        self.ui.btn_plus.clicked.connect(lambda: self.add_temp('+'))
        self.ui.btn_min.clicked.connect(lambda: self.add_temp('-'))
        self.ui.btn_multy.clicked.connect(lambda: self.add_temp('*'))
        self.ui.btn_div.clicked.connect(lambda: self.add_temp('/'))

        self.ui.btn_backspace.clicked.connect(self.backspace)

    def add_digit(self, btn_text: str) -> str:
        self.clear_temp_if_equality()
        if self.ui.l_e.text() == '0':
            self.ui.l_e.setText(btn_text)
            return self.ui.l_e.text()

        else:
            self.ui.l_e.setText(self.ui.l_e.text() + btn_text)
            return self.ui.l_e.text()

    def speedName(self, btn):
        print(btn.sender)
        return btn.sender()

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.ui.lbl_temp.clear()

    def show_error(self, text: str) -> None:
        self.ui.l_e.setMaxLength(len(text))
        self.ui.l_e.setText(text)

    def click_btn(self):
        self.ui.btn_1.click()
        return self.ui.lbl_temp.text()

    def return_lbl_temp(self):
        return self.ui.lbl_temp.text()

    def clear_all(self) -> None:
        self.clear_temp_if_equality()
        self.ui.l_e.setText("0")
        self.ui.lbl_temp.clear()

    def set_date(self, str1: str, str2: str):
        self.ui.l_e.setText(str1)
        self.ui.lbl_temp.setText(str2)

    def clear_entry(self) -> None:
        self.clear_temp_if_equality()
        self.ui.l_e.setText("0")

    def negate(self):
        self.clear_temp_if_equality()
        entry = self.ui.l_e.text()
        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]
        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.ui.l_e.setMaxLength(self.entry_max_len + 1)
        else:
            self.ui.l_e.setMaxLength(self.entry_max_len)

        self.ui.l_e.setText(entry)

    def backspace(self) -> None:
        self.clear_temp_if_equality()
        entry = self.ui.l_e.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.l_e.setText('0')
            else:
                self.ui.l_e.setText(entry[:-1])
        else:
            self.ui.l_e.setText('0')

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        if '.' not in self.ui.l_e.text():
            self.ui.l_e.setText((self.ui.l_e.text() + '.'))

    @staticmethod
    def remove_trailing_zeros(num: Union[float, int, str]) -> str:
        n = str(float(num))
        # обрезаются нули,но не все
        return n[:-2] if n[-2:] == '.0' else n

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.l_e.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    # ПОЛУЧАЕМ ЧИСЛО ВО ВРЕМЕННОЙ СТРОКЕ
    # ЕСЛИ ЕСТЬ ТЕКСТ,ТО
    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    # ПОЛУЧАЕМ ЗНАК ОПЕРАЦИИ
    def get_math_sign(self) -> Optional[str]:
        # ЕСЛИ ВО ВРЕМЕННОЙ СТРОКЕ ЕСТЬ ТЕКСТ,ТО
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]

    def add_temp(self, math_sign: str) -> str:
        if not self.ui.lbl_temp.text() or self.get_math_sign() == '=':
            self.ui.lbl_temp.setText(self.remove_trailing_zeros(self.ui.l_e.text()) + f' {math_sign} ')
            self.ui.l_e.setText('0')
            return self.ui.lbl_temp.text()

    def calculate(self) -> Optional[str]:
        # В ПЕРЕМЕННУЮ ЗАПИСЫВАЕМ,ВСЕ ЧТО НАХОДИТСЯ ВО ВРЕМЕННОЙ СТРОКЕ И В ПОЛЕ ВВОДА
        entry = self.ui.l_e.text()
        print(entry)
        temp = self.ui.lbl_temp.text()
        # ЕСЛИ ВО ВРЕМЕННОЙ СТРОКЕ ЕСТЬ ЧТО-ТО
        if temp:
            try:
                # СЧИТАЕМ РЕЗУЛЬТАТ

                ##if self.get_math_sign() == '/' and self.get_entry_num() == 0:
                #    answer = "None"
                 #   self.ui.l_e.setText(answer)
                  #  return answer
               # else:
                    answer = self.remove_trailing_zeros(
                        str(result(self.get_math_sign(), self.get_temp_num(), self.get_entry_num())))
                    self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' = ')
                    self.ui.l_e.setText(answer)
                    return answer
            except KeyError:
                pass
            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error('error')
                else:
                    self.show_error('error')

    def math_operation(self, math_sign: str):
        temp = self.ui.lbl_temp.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{math_sign} ')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f' {math_sign}')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
