from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.count = 0

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Hello World')
        self.InitUI()

        self.backward_button = QtWidgets.QPushButton(self)
        self.backward_button.setIcon(QIcon("icons/backward_arrow_icon.png"))
        self.backward_button.setGeometry(10, 52, 30, 30)

        self.forward_button = QtWidgets.QPushButton(self)
        self.forward_button.setIcon(QIcon("icons/forward_arrow_icon.png"))
        self.forward_button.setGeometry(50, 52, 30, 30)

    def InitUI(self):
        self.prax_logo = QtWidgets.QLabel(self)
        self.prax_logo.setText("Prax Logo")
        self.prax_logo.move(550, 300)
        self.prax_logo.setStyleSheet("QLabel { color : blue; }")

        self.url_bar = QtWidgets.QLineEdit(self)
        self.url_bar.setGeometry(200, 50, 800, 35)

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

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setGeometry(100, 100, 1200, 800)
    win.setWindowTitle("Prax")



    win.show()
    sys.exit(app.exec_())

window()
