from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets

class UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 727)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setStyleSheet("QFrame#mainFrame {\n"
                                     "    background-color: rgb(45, 45, 45);\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainFrame.setLineWidth(0)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topBar = QtWidgets.QFrame(self.mainFrame)
        self.topBar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.topBar.setStyleSheet("background-color: none;\n"
"")
        self.topBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topBar.setObjectName("topBar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.topBar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.topFrame = QtWidgets.QFrame(self.topBar)
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topFrame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browserNameLabel = QtWidgets.QFrame(self.topFrame)
        self.browserNameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.browserNameLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.browserNameLabel.setObjectName("browserNameLabel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.browserNameLabel)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.browserName = QtWidgets.QLabel(self.browserNameLabel)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.browserName.setFont(font)
        self.browserName.setAutoFillBackground(False)
        self.browserName.setStyleSheet("color: rgb(200, 200, 200);")
        self.browserName.setObjectName("browserName")
        self.verticalLayout_5.addWidget(self.browserName)
        self.horizontalLayout.addWidget(self.browserNameLabel)
        self.verticalLayout_3.addWidget(self.topFrame)
        self.bottomFrame = QtWidgets.QFrame(self.topBar)
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bottomFrame.setLineWidth(0)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leftArrowBtn = QtWidgets.QPushButton(self.bottomFrame)
        self.leftArrowBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.leftArrowBtn.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Entypo")
        font.setPointSize(16)
        self.leftArrowBtn.setFont(font)
        self.leftArrowBtn.setStyleSheet("QPushButton {\n"
"    color: rgba(172, 172, 172, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(172, 172, 172, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.leftArrowBtn.setObjectName("leftArrowBtn")
        self.horizontalLayout_5.addWidget(self.leftArrowBtn)
        self.rightArrowBtn = QtWidgets.QPushButton(self.bottomFrame)
        self.rightArrowBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.rightArrowBtn.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Entypo")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rightArrowBtn.setFont(font)
        self.rightArrowBtn.setStyleSheet("QPushButton {\n"
"    color: rgba(172, 172, 172, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(172, 172, 172, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.rightArrowBtn.setObjectName("rightArrowBtn")
        self.horizontalLayout_5.addWidget(self.rightArrowBtn)
        self.reloadBtn = QtWidgets.QPushButton(self.bottomFrame)
        self.reloadBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.reloadBtn.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Entypo")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.reloadBtn.setFont(font)
        self.reloadBtn.setStyleSheet("QPushButton {\n"
"    color: rgba(172, 172, 172, 255);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(172, 172, 172, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.reloadBtn.setObjectName("reloadBtn")
        self.horizontalLayout_5.addWidget(self.reloadBtn)
        self.addressBar = QtWidgets.QLineEdit(self.bottomFrame)
        self.addressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.addressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(9)
        self.addressBar.setFont(font)
        self.addressBar.setStyleSheet("QLineEdit#addressBar {\n"
"    background-color: rgb(60, 60, 60);\n"
"    color: rgb(200, 200, 200);\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}")
        self.addressBar.setObjectName("addressBar")
        self.horizontalLayout_5.addWidget(self.addressBar)
        self.verticalLayout_3.addWidget(self.bottomFrame)
        self.verticalLayout_2.addWidget(self.topBar)
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.verticalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.browserName.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\">PraxBrowser</p></body></html>"))
        self.leftArrowBtn.setText(_translate("MainWindow", ""))
        self.rightArrowBtn.setText(_translate("MainWindow", ""))
        self.reloadBtn.setText(_translate("MainWindow", "⟳"))
        self.addressBar.setPlaceholderText(_translate("MainWindow", "Search with Google or enter address"))
