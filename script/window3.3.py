'''
@Description: 
@Version: 
@Autor: qc
@Date: 2020-01-06 00:13:40
@LastEditors: qc
@LastEditTime: 2020-03-13 19:42:33
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newproduct2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import pandas as pd
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 799)
        root = QtCore.QFileInfo(__file__).absolutePath()
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
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
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setGeometry(QtCore.QRect(330, 30, 891, 601))
        # self.graphicsView.setObjectName("graphicsView")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(50, 30, 1170, 601))
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

        # demo: 强制显示数据
        self.data = pd.read_csv('D:/jupyter_dir/yancao/data/adjust.csv')
        self.table_show(self.data)

        # # demo: 强制显示地图
        # self.image = mpimg.imread('D:/jupyter_dir/yancao/data/map.png') 
        # # Create widget
        # label = QLabel(self.graphicsView)
        # pixmap = QPixmap('D:/jupyter_dir/yancao/data/map.png')
        # label.setPixmap(pixmap)
        # # self.graphicsView.resize(pixmap.width(),pixmap.height())
        
        # self.graphicsView.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能化调整建议"))
        self.pushButton_3.setText(_translate("MainWindow", "确认修改到原策略"))
        self.pushButton_5.setText(_translate("MainWindow", "返回上一级"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSimple_Example.setText(_translate("MainWindow", "Simple example"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))

    def table_show(self, data):
        '''输入pd.DataFrame显示在sold_tableView'''
        model = PandasModel(data)
        self.tableView_2.setModel(model)



class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df.copy()

    def toDataFrame(self):
        return self._df.copy()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication