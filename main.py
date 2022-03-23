from PyQt5.QtWidgets import *

app = QApplication([]) #обязательная строка

###

window=QWidget() #окно
window1=QWidget()

#Создаем слой и располагаем элементы в ряд
layout = QVBoxLayout()
layout.addWidget(QPushButton('1')) #кнопка 1
layout.addWidget(QPushButton('2')) #кнопка 2
layout.addWidget(QPushButton('3')) #кнопка 3
layout.addWidget(QPushButton('4')) #кнопка 4


layout1 = QVBoxLayout()
layout1.addWidget(QPushButton('1')) #кнопка 1
layout1.addWidget(QPushButton('2')) #кнопка 2
layout1.addWidget(QPushButton('3')) #кнопка 3
layout1.addWidget(QPushButton('4')) #кнопка 4

#Размещаем слой в окне
window.setLayout(layout)
window1.setLayout(layout1)

window.show()
window1.show() # команда отображения на экране
app.exec_() # запустить приложение, пока пользователь не закроет его