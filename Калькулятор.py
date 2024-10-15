import sys

from PyQt6.QtWidgets import (QWidget, QPushButton,
                             QVBoxLayout, QLabel, QHBoxLayout, QApplication)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор')

        self.main_layout = QVBoxLayout()
        self.layout_1 = QHBoxLayout()
        self.layout_2 = QHBoxLayout()
        self.layout_3 = QHBoxLayout()
        self.layout_4 = QHBoxLayout()
        self.layout_5 = QHBoxLayout()

        self.secondary_label = QLabel()
        self.secondary_label.setEnabled(False)

        self.main_label = QLabel('0')
        self.main_label.setEnabled(False)

        self.number_buttons = []
        for i in range(10):
            btn = QPushButton(str(i))
            btn.clicked.connect(lambda checked, element=i: self.print_num(str(element)))
            self.number_buttons.append(btn)

        self.clear_button = QPushButton('C')
        self.clear_button.clicked.connect(self.clear_button_action)

        self.clear_entry_button = QPushButton('CE')
        self.clear_entry_button.clicked.connect(self.clear_entry_button_action)

        self.divide_button = QPushButton('/')
        self.divide_button.clicked.connect(lambda checked: self.print_action('/'))

        self.multiply_button = QPushButton('*')
        self.multiply_button.clicked.connect(lambda checked: self.print_action('*'))

        self.substract_button = QPushButton('-')
        self.substract_button.clicked.connect(lambda checked: self.print_action('-'))

        self.add_button = QPushButton('+')
        self.add_button.clicked.connect(lambda checked: self.print_action('+'))

        self.float_point_button = QPushButton('.')
        self.float_point_button.clicked.connect(lambda checked: self.print_num('.'))

        self.plus_minus_button = QPushButton('±')
        self.plus_minus_button.clicked.connect(self.plus_minus_button_action)

        self.equals_button = QPushButton('=')
        self.equals_button.clicked.connect(self.equal)

        self.layout_1.addWidget(self.number_buttons[7])
        self.layout_1.addWidget(self.number_buttons[8])
        self.layout_1.addWidget(self.number_buttons[9])
        self.layout_1.addWidget(self.divide_button)

        self.layout_2.addWidget(self.number_buttons[4])
        self.layout_2.addWidget(self.number_buttons[5])
        self.layout_2.addWidget(self.number_buttons[6])
        self.layout_2.addWidget(self.multiply_button)

        self.layout_3.addWidget(self.number_buttons[1])
        self.layout_3.addWidget(self.number_buttons[2])
        self.layout_3.addWidget(self.number_buttons[3])
        self.layout_3.addWidget(self.substract_button)

        self.layout_4.addWidget(self.clear_button)
        self.layout_4.addWidget(self.number_buttons[0])
        self.layout_4.addWidget(self.clear_entry_button)
        self.layout_4.addWidget(self.add_button)

        self.layout_5.addWidget(self.float_point_button)
        self.layout_5.addWidget(self.plus_minus_button)
        self.layout_5.addWidget(self.equals_button)

        self.main_layout.addWidget(self.secondary_label)
        self.main_layout.addWidget(self.main_label)
        self.main_layout.addLayout(self.layout_1)
        self.main_layout.addLayout(self.layout_2)
        self.main_layout.addLayout(self.layout_3)
        self.main_layout.addLayout(self.layout_4)
        self.main_layout.addLayout(self.layout_5)

        self.setLayout(self.main_layout)

    def clear_button_action(self):
        self.secondary_label.setText('')
        self.main_label.setText('0')

    def clear_entry_button_action(self):
        text = self.secondary_label.text().split()
        if text and (text[-1].isdigit() or '.' in text[-1]) and len(text) > 1:
            self.secondary_label.setText(' '.join(text[:-1]) + ' ')

    def print_num(self, i):
        if i == '0' and len(self.secondary_label.text()) > 1 and self.secondary_label.text().split()[-1] == '/':
            self.secondary_label.setText('')
            self.main_label.setText('ОШИБКА')

        else:
            if i == '.' and '.' in self.secondary_label.text().split()[-1]:
                pass

            else:

                self.secondary_label.setText(self.secondary_label.text() + i)

                if len(self.secondary_label.text().split()[-1]) > 30:
                    if self.secondary_label.text().split()[-1].isdigit():
                        self.secondary_label.setText(' '.join(self.secondary_label.text()[:-1]) +
                                                     ' ' + f'{int(self.secondary_label.text().split()[-1]):.2e}')

                    elif '.' in self.secondary_label.text().split()[-1]:
                        self.secondary_label.setText(' '.join(self.secondary_label.text()[:-1]) +
                                                     ' ' + f'{float(self.secondary_label.text().split()[-1]):.2e}')

                if len(str(int(eval(self.secondary_label.text())))) > 11:
                    n = f'{eval(self.secondary_label.text()):.2e}'
                else:
                    n = str(eval(self.secondary_label.text()))

                if float(n) == int(float(n)) and 'e' not in n:
                    self.main_label.setText(str(int(float(n))))
                else:
                    self.main_label.setText(n.replace('+', ''))

    def print_action(self, i):
        self.secondary_label.setText(self.secondary_label.text() + ' ' + i + ' ')

    def equal(self):
        self.secondary_label.setText('')

    def plus_minus_button_action(self):
        text = self.secondary_label.text().split()
        if text[-1] == '+':
            self.secondary_label.setText(' '.join(text[:-1]) + ' ' + '-' + ' ')
        elif text[-1] == '-':
            self.secondary_label.setText(' '.join(text[:-1]) + ' ' + '+' + ' ')
        elif float(text[-1]) != 0:
            if len(text) == 1 and all(i.isdigit() for i in text[-1].split('.')):
                self.secondary_label.setText('- ' + text[-1])
            else:
                if text[-2] == '+':
                    self.secondary_label.setText(' '.join([' '.join(text[:-2]), '-', text[-1]]))
                elif text[-2] == '-':
                    if len(text) == 2 and text[-1].isdigit():
                        self.secondary_label.setText(text[-1])
                    else:
                        self.secondary_label.setText(' '.join([' '.join(text[:-2]), '+', text[-1]]))
        self.main_label.setText(str(eval(self.secondary_label.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
