'''
@Description: 
@Version: 
@Autor: qc
@Date: 2020-01-05 23:53:42
@LastEditors: qc
@LastEditTime: 2020-03-27 17:16:24
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newproduct1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 799)
        root = QtCore.QFileInfo(__file__).absolutePath()
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 221, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 580, 221, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(265, 31, 951, 601))
        self.tableView.setObjectName("tableView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1020, 650, 201, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 140, 221, 51))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 650, 201, 51))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
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
        self.data = pd.read_csv('D:/jupyter_dir/yancao/data/recommend.csv')
        self.table_show(self.data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能化新品选点"))
        self.pushButton.setText(_translate("MainWindow", "1.上传参考城市数据"))
        self.pushButton_2.setText(_translate("MainWindow", "3.生成建议投放零售户"))
        self.pushButton_3.setText(_translate("MainWindow", "5.导出表格文件"))
        self.pushButton_4.setText(_translate("MainWindow", "2.上传目标城市数据"))
        self.pushButton_5.setText(_translate("MainWindow", "4.查看地图分布"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSimple_Example.setText(_translate("MainWindow", "Simple example"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
        
    def table_show(self, data):
        '''输入pd.DataFrame显示在sold_tableView'''
        model = PandasModel(data)
        self.tableView.setModel(model)

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