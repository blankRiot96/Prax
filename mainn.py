from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5 import QtCore, QtWidgets
from ParaxBrowserUI import UI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import sys

GLOBAL_STATE = 0

class ParaxBrowser(QtWidgets.QMainWindow, UI):
    def __init__(self):
        super(ParaxBrowser, self).__init__()
        self.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.maximizeBtn.clicked.connect(lambda: self.maximizeRestore())
        self.minimizeBtn.clicked.connect(lambda: self.showMinimized())
        self.closeBtn.clicked.connect(lambda: self.close())

        self.browserName.mouseMoveEvent = self.moveWindow
        self.titleBar.mouseMoveEvent = self.moveWindow
        self.topFrame.mouseMoveEvent = self.moveWindow

        self.addressBar.returnPressed.connect(self.loadPage)

        self.reloadBtn.clicked.connect(self.reload)
        self.leftArrowBtn.clicked.connect(self.backward)
        self.rightArrowBtn.clicked.connect(self.forward)

    def loadPage(self):
        url = QtCore.QUrl.fromUserInput(self.addressBar.text())
        #  search = str(url)[26:-2]
        search = self.addressBar.text()
        search.replace(' ', '+')

        if url.isValid():
            self.webEngineView.load(url)
        else:
            self.webEngineView.load(QtCore.QUrl('https://www.google.com/search?q=' + search))

    
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def moveWindow(self, event):
            if self.returnStatus == 1:
                self.maximizeRestore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def maximizeRestore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.mainFrame.setStyleSheet("QFrame#mainFrame {\n""    background-color: rgb(43, 43, 43);\n""    border-radius: 0px; \n""}")
            self.maximizeBtn.setToolTip("Restore Down")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.verticalLayout.setContentsMargins(10, 10, 10, 10)
            self.mainFrame.setStyleSheet("QFrame#mainFrame {\n""    background-color: rgb(43, 43, 43);\n""    border-radius: 10px; \n""}")
            self.maximizeBtn.setToolTip("Maximize")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus():
        return GLOBAL_STATE

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = ParaxBrowser()
    Window.show()
    app.exec_()
