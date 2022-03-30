from PyQt5.QtWidgets import *
from pyownmod import *
app = QApplication([]) #обязательная строка

btn1 = QPushButton("Минимальная")
btn2 = QPushButton("Максимальная")
btn3 = QPushButton("Текущая")

rad1 = QRadioButton('Киров')
rad2 = QRadioButton('Москва')
rad3 = QRadioButton('Казань')


class Form(QWidget):
    def initForm(self):
        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(rad1)
        layout.addWidget(rad2)
        layout.addWidget(rad3)
        self.setLayout(layout)
        self.show()


window=Form()
window.initForm()

def onRad1():
    rad1.setChecked(True)
    if rad1.isChecked():
        x = 'Kirov'

def onRad2():
    rad2.setChecked(True)
    if rad2.isChecked():
        x = 'Moscow'

def onRad3():
    rad3.setChecked(True)
    if rad3.isChecked():
        x = 'Kazan'




def on_click1():
    OWMMOD1(x)
def on_click2():
    OWMMOD2(x)
def on_click3():
    OWMMOD3(x)

btn1.clicked.connect(on_click3)
btn2.clicked.connect(on_click2)
btn3.clicked.connect(on_click1)



app.exec_() # запустить приложение, пока пользователь не закроет его