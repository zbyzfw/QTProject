# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boxui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(12, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setMinimumSize(QtCore.QSize(116, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.toolBox.setObjectName("toolBox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 150, 367))
        self.page_3.setObjectName("page_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 150, 367))
        self.page_4.setObjectName("page_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 9, 111, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        self.toolBox.addItem(self.page_4, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 185))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 112))
        self.widget.setObjectName("widget")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 131, 111))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 100))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_openFile = QtWidgets.QPushButton(self.page_2)
        self.btn_openFile.setObjectName("btn_openFile")
        self.gridLayout_4.addWidget(self.btn_openFile, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.btn_train = QtWidgets.QPushButton(self.page_2)
        self.btn_train.setObjectName("btn_train")
        self.gridLayout_4.addWidget(self.btn_train, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_openFile_2 = QtWidgets.QPushButton(self.page_6)
        self.btn_openFile_2.setObjectName("btn_openFile_2")
        self.gridLayout_5.addWidget(self.btn_openFile_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.btn_test = QtWidgets.QPushButton(self.page_6)
        self.btn_test.setObjectName("btn_test")
        self.gridLayout_5.addWidget(self.btn_test, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionSet = QtWidgets.QAction(MainWindow)
        self.actionSet.setObjectName("actionSet")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionclose)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSet)
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)
        self.actionHelp.triggered.connect(MainWindow.trigger_actHelp)
        self.pushButton_2.clicked.connect(MainWindow.click_pushButton_1)
        self.pushButton_1.clicked.connect(MainWindow.click_pushButton_2)
        self.pushButton_4.clicked.connect(MainWindow.click_pushButton_4)
        self.pushButton_3.clicked.connect(MainWindow.click_pushButton_3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "????????????"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????"))
        self.pushButton_9.setText(_translate("MainWindow", "????????????1"))
        self.pushButton_1.setText(_translate("MainWindow", "????????????2"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn_openFile.setText(_translate("MainWindow", "?????????????????????"))
        self.btn_train.setText(_translate("MainWindow", "????????????"))
        self.btn_openFile_2.setText(_translate("MainWindow", "?????????????????????"))
        self.btn_test.setText(_translate("MainWindow", "??????????????????"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "??????"))
        self.actionSave.setText(_translate("MainWindow", "??????"))
        self.actionclose.setText(_translate("MainWindow", "??????"))
        self.actionSet.setText(_translate("MainWindow", "??????"))
        self.actionHelp.setText(_translate("MainWindow", "??????"))
