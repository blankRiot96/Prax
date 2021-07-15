from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets


class UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setStyleSheet("QFrame#mainFrame {\n"
                                     "    background-color: rgb(45, 45, 45);\n"
                                     "    border-radius: 10px; \n"
                                     "}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainFrame.setLineWidth(0)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleBar = QtWidgets.QFrame(self.mainFrame)
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titleBar.setStyleSheet("background-color: none;\n"
                                    "")
        self.titleBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleBar.setObjectName("titleBar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.titleBar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.topFrame = QtWidgets.QFrame(self.titleBar)
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
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
        self.buttons = QtWidgets.QFrame(self.topFrame)
        self.buttons.setMaximumSize(QtCore.QSize(100, 16777215))
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimizeBtn = QtWidgets.QPushButton(self.buttons)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(16, 16))
        self.minimizeBtn.setMaximumSize(QtCore.QSize(17, 17))
        self.minimizeBtn.setStyleSheet("QPushButton {\n"
                                       "border: none;\n"
                                       "border-radius: 8px;\n"
                                       "background-color: rgb(24, 205, 75);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgba(24, 205, 75, 150);\n"
                                       "}")
        self.minimizeBtn.setText("")
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_2.addWidget(self.minimizeBtn)
        self.maximizeBtn = QtWidgets.QPushButton(self.buttons)
        self.maximizeBtn.setMinimumSize(QtCore.QSize(16, 16))
        self.maximizeBtn.setMaximumSize(QtCore.QSize(17, 17))
        self.maximizeBtn.setStyleSheet("QPushButton {\n"
                                       "border: none;\n"
                                       "border-radius: 8px;\n"
                                       "    background-color: rgb(254, 195, 68);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgba(254, 195, 68, 150);\n"
                                       "}")
        self.maximizeBtn.setText("")
        self.maximizeBtn.setObjectName("maximizeBtn")
        self.horizontalLayout_2.addWidget(self.maximizeBtn)
        self.closeBtn = QtWidgets.QPushButton(self.buttons)
        self.closeBtn.setMinimumSize(QtCore.QSize(16, 16))
        self.closeBtn.setMaximumSize(QtCore.QSize(17, 17))
        self.closeBtn.setStyleSheet("QPushButton {\n"
                                    "border: none;\n"
                                    "border-radius: 8px;\n"
                                    "background-color: rgb(255, 82, 85);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgba(255, 82, 85, 100);\n"
                                    "}")
        self.closeBtn.setText("")
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_2.addWidget(self.closeBtn)
        self.horizontalLayout.addWidget(self.buttons)
        self.verticalLayout_3.addWidget(self.topFrame)
        self.bottomFrame = QtWidgets.QFrame(self.titleBar)
        self.bottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomFrame.setObjectName("bottomFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 2)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.leftArrowBtn = QtWidgets.QPushButton(self.bottomFrame)
        self.leftArrowBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.leftArrowBtn.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Entypo")
        font.setPointSize(13)
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
        font.setPointSize(13)
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
        font.setPointSize(12)
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
        self.verticalLayout_2.addWidget(self.titleBar)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ParaxBrowser"))
        self.browserName.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\">                ParaxBrowser</p></body></html>"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Minimize</p></body></html>"))
        self.maximizeBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Maximize</p></body></html>"))
        self.closeBtn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Close</p></body></html>"))
        self.leftArrowBtn.setText(_translate("MainWindow", ""))
        self.rightArrowBtn.setText(_translate("MainWindow", ""))
        self.reloadBtn.setText(_translate("MainWindow", "⟳"))
        self.addressBar.setPlaceholderText(_translate("MainWindow", "Search with Google or enter address"))
