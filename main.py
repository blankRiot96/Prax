from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
from PyQt5.QtGui import QIcon

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.count = 0

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Hello World')
        self.InitUI()


        # self.photo = QtWidgets.QLabel(self)
        # self.photo.setGeometry(0, 0, 1200, 800)
        # self.photo.setText("")
        # self.photo.setPixmap(QtGui.QPixmap("images/gradient.jpeg"))

        self.backward_button = QtWidgets.QPushButton(self)
        #self.backward_button.setIcon(QIcon("icons/backward_arrow_icon.png"))
        self.backward_button.setStyleSheet("border-image : url(images/icons/backward_arrow_icon.png);")
        self.backward_button.setGeometry(10, 52, 25, 25)

        self.forward_button = QtWidgets.QPushButton(self)
        #self.forward_button.setIcon(QIcon("icons/forward_arrow_icon.png"))
        self.forward_button.setStyleSheet("border-image : url(images/icons/forward_arrow_icon.png);")
        self.forward_button.setGeometry(60, 52, 25, 25)


    def InitUI(self):
        self.prax_logo = QtWidgets.QLabel(self)
        self.prax_logo.setText("Prax Logo")
        self.prax_logo.move(550, 300)
        self.prax_logo.setStyleSheet("QLabel { color : blue; }")

        self.url_bar = QtWidgets.QLineEdit(self)
        self.url_bar.setGeometry(100, 50, 1000, 25)

        # self.b1 = QtWidgets.QPushButton(self)
        # self.b1.setText("Click me!")
        # self.b1.move(100, 100)
        # self.b1.clicked.connect(self.changeText)

    # def changeText(self):
        # self.label.setText(f'Changed Text {self.count}')
        # self.update()
        # self.count += 1

    # def update(self):
        # self.label.adjustSize()



# def clik():
    # print("Clicked")


with open('styling.qss', 'r') as f:
    style = f.read()

def window():
    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    win = MyWindow()
    win.setGeometry(100, 100, 1200, 800)
    win.setWindowTitle("Prax")



    win.show()
    sys.exit(app.exec_())

window()
