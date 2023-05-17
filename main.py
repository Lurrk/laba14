def laba14_1():

    import sys
    import requests
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLineEdit, QLabel, QPushButton

    class CurrencyConverter(QWidget):
        api_key = 'sw4GNH3gcZlrvPbBbEMT1ZOSDB3K4eBp'

        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            layout = QVBoxLayout()

            self.amount_input = QLineEdit()
            layout.addWidget(self.amount_input)

            self.from_currency_cb = QComboBox()
            self.from_currency_cb.addItems(["USD", "EUR", "RUB"])
            layout.addWidget(self.from_currency_cb)

            self.to_currency_cb = QComboBox()
            self.to_currency_cb.addItems(["USD", "EUR", "RUB"])
            layout.addWidget(self.to_currency_cb)

            self.result_label = QLabel()
            layout.addWidget(self.result_label)

            convert_button = QPushButton("Convert")
            convert_button.clicked.connect(self.convert)
            layout.addWidget(convert_button)

            self.setLayout(layout)
            self.setWindowTitle("Currency Converter")

        def convert(self):
            amount = float(self.amount_input.text())
            from_currency = self.from_currency_cb.currentText()
            to_currency = self.to_currency_cb.currentText()

            if from_currency == to_currency:
                self.result_label.setText(f"{amount} {from_currency}")
                return

            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"  # ?access_key={self.api_key}
            headers = {f'apikey': self.api_key}
            response = requests.get(url, headers=headers)
            converted_amount = response.json()["result"]
            self.result_label.setText(f"{converted_amount:.2f} {to_currency}")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        converter = CurrencyConverter()
        converter.show()
        sys.exit(app.exec_())

def laba14_2():
    import sys
    from PyQt5.Qt import QApplication, QWidget, QLabel, QLineEdit, QPushButton

    class BMI(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):

            self.weight_label = QLabel('Вес (кг):', self)
            self.weight_label.move(50, 50)
            self.weight_label.resize(self.weight_label.sizeHint())

            self.weight_input = QLineEdit(self)
            self.weight_input.move(150, 50)
            self.weight_input.resize(100, 20)

            self.height_label = QLabel('Рост (см):', self)
            self.height_label.move(50, 80)
            self.height_label.resize(self.height_label.sizeHint())

            self.height_input = QLineEdit(self)
            self.height_input.move(150, 80)
            self.height_input.resize(100, 20)

            self.calculate_button = QPushButton('Рассчитать', self)
            self.calculate_button.move(150, 110)
            self.calculate_button.clicked.connect(self.calculate_bmi)

            self.bmi_label = QLabel('Индекс массы тела:', self)
            self.bmi_label.move(50, 150)
            self.bmi_label.resize(self.bmi_label.sizeHint())

            self.bmi_result = QLabel('', self)
            self.bmi_result.move(200, 150)
            self.bmi_result.resize(self.bmi_result.sizeHint())

            self.advice_label = QLabel('Фаза:', self)
            self.advice_label.move(50, 180)
            self.advice_label.resize(self.advice_label.sizeHint())

            self.advice_result = QLabel('', self)
            self.advice_result.move(200, 180)
            self.advice_result.resize(self.advice_result.sizeHint())

            self.setGeometry(100, 100, 400, 300)
            self.setWindowTitle('Индекс массы тела')
            self.show()

        def calculate_bmi(self):

            weight = float(self.weight_input.text())
            height = float(self.height_input.text()) / 100
            bmi = round(weight / (height * height), 2)
            self.bmi_result.setText(str(bmi))

            if bmi < 18.5:
                advice = 'ЖРИ БОЛЬШЕ'
            elif 18.5 <= bmi <= 24.9:
                advice = 'КРАСАВА'
            elif 25 <= bmi <= 29.9:
                advice = 'Сегодня без ужина'
            else:
                advice = 'ЖРИ МЕНЬШЕ'

            self.advice_result.setText(advice)
            self.advice_result.resize(self.advice_result.sizeHint())

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        bmi = BMI()
        sys.exit(app.exec_())


laba14_2()