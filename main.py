from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5 import QtCore, QtWidgets
from PraxBrowserUI import UI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class ParaxBrowser(QtWidgets.QMainWindow, UI):
    def __init__(self):
        super(ParaxBrowser, self).__init__()
        self.setupUi(self)

        self.addressBar.returnPressed.connect(self.loadPage)

    def loadPage(self):
        url = QtCore.QUrl.fromUserInput(self.addressBar.text())
        search = self.addressBar.text()
        search.replace(' ', '+')
        if url.isValid():
            self.webEngineView.load(url)
        else:
            self.webEngineView.load(QtCore.QUrl(
                f'https://www.google.com/search?q={search}'))

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    # Menu Bar Setup
    self.menuBar_active = True
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
    # Connecting "alt" key to this ^ function

    def hide_show_menu_bar(self, menuBar, menuBar_active):
        if(menuBar_active == True):
            menuBar.hide()
            self.menuBar_active = False
            print("here 1")
        else:
            menuBar.show()
            self.menuBar_active = True




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = ParaxBrowser()
    Window.show()
    app.exec_()
