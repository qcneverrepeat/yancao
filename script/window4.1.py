'''
@Description: 
@Version: 
@Autor: qc
@Date: 2020-01-06 10:36:49
@LastEditors  : qc
@LastEditTime : 2020-01-06 11:01:32
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4.1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 811)
        root = QtCore.QFileInfo(__file__).absolutePath()
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
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


        # demo: 强制显示数据
        
        self.data1 = pd.read_csv('D:/jupyter_dir/yancao/data/replace1.csv')
        self.data2 = pd.read_csv('D:/jupyter_dir/yancao/data/replace2.csv')
        model_1 = PandasModel(self.data1)
        model_2 = PandasModel(self.data2)
        self.tableView.setModel(model_2)
        self.tableView_2.setModel(model_1)
    

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