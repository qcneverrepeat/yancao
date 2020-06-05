'''
@Description: 
@Version: 
@Autor: qc
@Date: 2020-04-26 14:31:44
@LastEditors: qc
@LastEditTime: 2020-04-26 16:42:30
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main++.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fun1 = QtWidgets.QPushButton(self.centralwidget)
        self.fun1.setGeometry(QtCore.QRect(230, 150, 311, 111))
        self.fun1.setMinimumSize(QtCore.QSize(311, 111))
        self.fun1.setMaximumSize(QtCore.QSize(311, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.fun1.setFont(font)
        self.fun1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fun1.setObjectName("fun1")
        self.fun2 = QtWidgets.QPushButton(self.centralwidget)
        self.fun2.setGeometry(QtCore.QRect(230, 280, 311, 111))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.fun2.setFont(font)
        self.fun2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fun2.setObjectName("fun2")
        self.fun3 = QtWidgets.QPushButton(self.centralwidget)
        self.fun3.setGeometry(QtCore.QRect(230, 420, 311, 111))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.fun3.setFont(font)
        self.fun3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fun3.setObjectName("fun3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 381, 101))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fun3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.fun3_2.setGeometry(QtCore.QRect(230, 560, 311, 111))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.fun3_2.setFont(font)
        self.fun3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fun3_2.setObjectName("fun3_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " 智投放V1.0"))
        self.fun1.setText(_translate("MainWindow", "自动化 常规投放"))
        self.fun2.setText(_translate("MainWindow", "智能化 常规投放"))
        self.fun3.setText(_translate("MainWindow", "智能化 新品选点"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#043193;\">欢迎使用 智投放系统！</span></p></body></html>"))
        self.fun3_2.setText(_translate("MainWindow", "智能化 补货替代"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action_2.setText(_translate("MainWindow", "关于"))
        self.action_3.setText(_translate("MainWindow", "帮助"))
        self.action_4.setText(_translate("MainWindow", "退出"))
