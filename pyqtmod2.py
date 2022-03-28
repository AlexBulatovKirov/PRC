from PyQt5.QtWidgets import *
from pyownmod import OWMMOD
app = QApplication([]) #обязательная строка
window=QWidget() #окно
#Создаем кнопки
btn1 = QPushButton("Погода в Кирове")

#Создаем слой и располагаем элементы в ряд
layout = QVBoxLayout()
layout.addWidget(btn1) #кнопка 1
layout.addWidget(QPushButton('2')) #кнопка 2
layout.addWidget(QPushButton('3')) #кнопка 3
layout.addWidget(QPushButton('4')) #кнопка 4
#Размещаем слой в окне
window.setLayout(layout)


def on_click():
    layout.addWidget(QPushButton('5'))
    OWMMOD()
a = btn1.clicked.connect(on_click)




# команда отображения на экране
window.show()
app.exec_() # запустить приложение, пока пользователь не закроет его