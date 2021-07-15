from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Hello World')
        self.new_window_UI()

        # Menu Bar Setup
        menuBar_position = True
        menuBar = self.menuBar()
        # Creating menus ( like the order of FireFox )
        # Needs to add "actions" for every menu
        file_menu = menuBar.addMenu("&File")
        edit_menu = menuBar.addMenu("&Edit")
        view_menu = menuBar.addMenu("&View")
        history_menu = menuBar.addMenu("&History")
        bookmarks_menu = menuBar.addMenu("&Bookmarks")
        tools_menu = menuBar.addMenu("&Tools")
        help_menu = menuBar.addMenu("&Help") 

    # Used when Alt is pressed to hide or show the Menu Bar ( Used so often in softwares )         
    def hide_show_menu_bar(self, menuBar, menuBar_position):
        if(menuBar_position == True):
            menuBar.hide()
            menuBar_position = False
        else:
            menuBar.show()
            menuBar_position = True

    # need to connect "alt" key to this function
    # ...
            

    def new_window_UI(self):
        self.backward_button = QtWidgets.QPushButton(self)
        #self.backward_button.setIcon(QIcon("icons/backward_arrow_icon.png"))
        self.backward_button.setStyleSheet("border-image : url(images/icons/backward_arrow_icon.png);")
        self.backward_button.setGeometry(10, 52, 25, 25)

        self.forward_button = QtWidgets.QPushButton(self)
        #self.forward_button.setIcon(QIcon("icons/forward_arrow_icon.png"))
        self.forward_button.setStyleSheet("border-image : url(images/icons/forward_arrow_icon.png);")
        self.forward_button.setGeometry(60, 52, 25, 25)

        self.prax_logo = QtWidgets.QLabel(self)
        self.prax_logo.setText("Prax Logo")
        self.prax_logo.move(550, 300)
        self.prax_logo.setStyleSheet("QLabel { color : blue; }")

        self.url_bar = QtWidgets.QLineEdit(self)
        self.url_bar.setGeometry(100, 50, 1000, 25)


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
