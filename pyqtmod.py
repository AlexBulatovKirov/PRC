from PyQt5.QtWidgets import *
app = QApplication([]) #обязательная строка
window=QWidget() #окно
#Создаем слой и располагаем элементы в ряд
layout = QVBoxLayout()
layout.addWidget(QPushButton('Первая кнопка')) #кнопка 1
layout.addWidget(QPushButton('2')) #кнопка 2
layout.addWidget(QPushButton('3')) #кнопка 3
layout.addWidget(QPushButton('4')) #кнопка 4
#Размещаем слой в окне
window.setLayout(layout)
# команда отображения на экране
window.show()
app.exec_() # запустить приложение, пока пользователь не закроет его