'''
@Description: 
@Version: 
@Autor: qc
@Date: 2020-01-05 22:36:27
@LastEditors: qc
@LastEditTime: 2020-04-26 13:32:43
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main+.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        root = QtCore.QFileInfo(__file__).absolutePath()
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
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
        self.fun2.clicked.connect(self.smart_put)
        self.fun3 = QtWidgets.QPushButton(self.centralwidget)
        self.fun3.setGeometry(QtCore.QRect(230, 420, 311, 111))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.fun3.setFont(font)
        self.fun3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fun3.setObjectName("fun3")
        self.fun3.clicked.connect(self.smart_put)
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
        self.fun3_2.clicked.connect(self.smart_put)
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

    def smart_put(self):
        '''智能化投放仍在开发'''
        QMessageBox.information(self, '提示', '此功能属于智能化投放部分，尚在开发，敬请期待')
        # QMessageBox.warning(self, '警告','三率一面数据中品规名和ID不匹配：ID6901028051989-云烟(软大重九)')
        
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication
