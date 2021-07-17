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

        # Menu Bar Setup
        self.menuBar_active = True
        self.menuBar = QMenuBar()

        # Creating menus ( like the order of FireFox )
        # Needs to add "actions" for every menu
        file_menu = QMenu("&File", self)  # self.menuBar.addMenu("&File")
        edit_menu = QMenu("&Edit", self)
        view_menu = QMenu("&View", self)
        history_menu = QMenu("&History", self)
        bookmarks_menu = QMenu("&Bookmarks", self)
        tools_menu = QMenu("&Tools", self)
        help_menu = QMenu("&Help", self)

        # Adding menu bar
        self.menuBar.addMenu(file_menu)
        self.menuBar.addMenu(edit_menu)
        self.menuBar.addMenu(view_menu)
        self.menuBar.addMenu(history_menu)
        self.menuBar.addMenu(bookmarks_menu)
        self.menuBar.addMenu(tools_menu)
        self.menuBar.addMenu(help_menu)

        self.setMenuBar(self.menuBar)

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

    # Connecting "alt" key to this ^ function
    def hide_show_menu_bar(self):
        if self.menuBar_active:
            self.menuBar.hide()
            self.menuBar_active = False
            print("here 1")
        else:
            self.menuBar.show()
            self.menuBar_active = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = ParaxBrowser()
    Window.show()
    app.exec_()
