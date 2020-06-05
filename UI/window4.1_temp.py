# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4.1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 811)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(390, 100, 831, 551))
        self.tableView.setObjectName("tableView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1010, 680, 211, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 30, 221, 51))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 30, 221, 51))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(50, 100, 311, 551))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "智能化补货替代"))
        self.pushButton_3.setText(_translate("MainWindow", "3.导出表格文件"))
        self.pushButton_6.setText(_translate("MainWindow", "2.生成替代品规列表"))
        self.pushButton_7.setText(_translate("MainWindow", "1.导入缺货品规"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSimple_Example.setText(_translate("MainWindow", "Simple example"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
