import sys
# This code block is not needed. Run "pip install PyQt5" in the terminal instead.

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculadora Simples')
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        grid_layout = QVBoxLayout()

        for i in range(4):
            row_layout = QVBoxLayout()
            for j in range(4):
                button = QPushButton(buttons[i * 4 + j])
                button.clicked.connect(self.on_button_click)
                row_layout.addWidget(button)
            grid_layout.addLayout(row_layout)

        self.layout.addLayout(grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self):
        clicked_button = self.sender()
        text = clicked_button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Erro')
        elif text == 'C':
            self.display.clear()
        else:
            current_text = self.display.text()
            self.display.setText(current_text + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
