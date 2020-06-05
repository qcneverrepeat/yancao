# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newproduct2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1020, 650, 201, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 650, 201, 51))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(330, 30, 891, 601))
        self.graphicsView.setObjectName("graphicsView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(40, 30, 271, 601))
        self.tableView_2.setObjectName("tableView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSimple_Example = QtWidgets.QAction(MainWindow)
        self.actionSimple_Example.setObjectName("actionSimple_Example")
        self.actionAbout_us = QtWidgets.QAction(MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.menu.addSeparator()
        self.menu.addAction(self.actionSimple_Example)
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionExit)
        self.menu.addAction(self.actionAbout_us)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "导出表格文件"))
        self.pushButton_5.setText(_translate("MainWindow", "返回上一级"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSimple_Example.setText(_translate("MainWindow", "Simple example"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
