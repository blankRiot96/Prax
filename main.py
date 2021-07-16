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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = ParaxBrowser()
    Window.show()
    app.exec_()
