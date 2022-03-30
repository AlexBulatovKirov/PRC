from PyQt5.QtWidgets import *
from pyownmod import *

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

    def initForm(self):

        self.layout.addWidget(btn1)
        self.layout.addWidget(btn2)
        self.layout.addWidget(btn3)
        self.layout.addWidget(rad1)
        self.layout.addWidget(rad2)
        self.layout.addWidget(rad3)

        self.setLayout(self.layout)
        self.show()

    def text(self,temp):
        self.temp = temp
        self.layout.addWidget(QPushButton(self.temp))
        self.show()



app = QApplication([])

btn1 = QPushButton("Текущая")
btn2 = QPushButton("Максимальная")
btn3 = QPushButton("Минимальная")
rad1 = QRadioButton('Киров')
rad2 = QRadioButton('Москва')
rad3 = QRadioButton('Казань')
window = Form()

window.initForm()
if __name__ == '__main__':






    def on_click1():

        if rad1.isChecked() == True:
            window.text(str(OWMMOD1('Kirov')))
        elif rad2.isChecked() == True:
            window.text(str(OWMMOD1('Moscow')))
        elif rad3.isChecked() == True:
            window.text(str(OWMMOD1('Kazan')))

    def on_click2():

        if rad1.isChecked() == True:
            window.text(str(OWMMOD2('Kirov')))

        elif rad2.isChecked() == True:
            window.text(str(OWMMOD2('Moscow')))
        elif rad3.isChecked() == True:
            window.text(str(OWMMOD2('Kazan')))

    def on_click3():

        if rad1.isChecked() == True:
            window.text(str(OWMMOD3('Kirov')))
        elif rad2.isChecked() == True:
            window.text(str(OWMMOD2('Moscow')))
        elif rad3.isChecked() == True:
            window.text(str(OWMMOD3('Kazan')))

    btn1.clicked.connect(on_click1)
    btn2.clicked.connect(on_click2)
    btn3.clicked.connect(on_click3)

app.exec_()



