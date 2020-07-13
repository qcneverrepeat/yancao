# -*- coding: utf-8 -*-

import sys
import os
import webbrowser
import json
import copy
import numpy as np 
import pandas as pd
import cplex
from PyQt5 import QtCore, QtGui, QtWidgets
import xlrd

# 初始化全局变量para：读取parameter.json（上次的参数设置）,万一文件不存在则赋原始默认值
try:
    f = open('parameter.json')
    para = json.load(f)
except:
    para = {'delta_sold':0.01, 'slym_w':[3,3,1,0.1], 'slym_o':[0.5,0.5,0.8,0.5], 'thre':[-0.8,0.8], 'beta':0.3, 'alpha':0.12}

class Ui_Start(QtWidgets.QMainWindow):
    '''主窗口类: 自动化、智能化、...'''
    def setupUi(self, Start):
        Start.setObjectName("MainWindow")
        if getattr(sys, 'frozen', False):
            root = os.path.dirname(sys.executable)
        else:
            root = QtCore.QFileInfo(__file__).absolutePath() # __file__是文件名字符串
        Start.setWindowIcon(QtGui.QIcon(root+'/fav.ico'))
        Start.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(Start)
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
        self.fun1.clicked.connect(self.auto_put) # 点击进入一级窗口，自动化投放

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

        Start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Start)
        self.statusbar.setObjectName("statusbar")
        Start.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(Start)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(Start)
        self.action_3.setObjectName("action_3")
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.action_2.triggered.connect(self.about)
        self.action_3.triggered.connect(QtWidgets.QApplication.quit)

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

    def retranslateUi(self, Start):
        _translate = QtCore.QCoreApplication.translate
        Start.setWindowTitle(_translate("MainWindow", " 智投放V1.2"))
        self.fun1.setText(_translate("MainWindow", "自动化 常规投放"))
        self.fun2.setText(_translate("MainWindow", "智能化 常规投放"))
        self.fun3.setText(_translate("MainWindow", "智能化 新品选点"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#043193;\">欢迎使用 智投放系统！</span></p></body></html>"))
        self.fun3_2.setText(_translate("MainWindow", "智能化 补货替代"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action_2.setText(_translate("MainWindow", "关于"))
        self.action_3.setText(_translate("MainWindow", "退出"))

    def smart_put(self):
        '''智能化投放仍在开发'''
        QtWidgets.QMessageBox.information(self, '提示', '此功能属于智能化投放部分，尚在开发，敬请期待')

    def about(self):
        '''关于我们'''
        self.about_window = QtWidgets.QWidget()
        self.ui3 = Ui_About()
        self.ui3.setupUi(self.about_window)
        self.about_window.show()

    def auto_put(self):
        '''点击调用一级窗口类'''
        self.sub_window = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self.sub_window) # 此步中初始化了一级窗口类中的self.para，类似__init__的作用
        self.sub_window.show()


class Ui_MainWindow(QtWidgets.QMainWindow):
    '''一级窗口类'''    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 800)
        if getattr(sys, 'frozen', False):
            root = os.path.dirname(sys.executable)
        else:
            root = QtCore.QFileInfo(__file__).absolutePath() # __file__是文件名字符串
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/fav.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 1.输入销量目标
        self.input_sold_obj = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sold_obj.setGeometry(QtCore.QRect(40, 30, 221, 51))
        self.input_sold_obj.setText("")
        self.input_sold_obj.setMaxLength(32766)
        self.input_sold_obj.setAlignment(QtCore.Qt.AlignCenter)
        self.input_sold_obj.setObjectName("input_sold_obj")

        # 2.输入结构目标
        self.input_price_obj = QtWidgets.QLineEdit(self.centralwidget)
        self.input_price_obj.setGeometry(QtCore.QRect(40, 110, 221, 51))
        self.input_price_obj.setText("")
        self.input_price_obj.setAlignment(QtCore.Qt.AlignCenter)
        self.input_price_obj.setObjectName("input_price_obj")

        # 3.上传上期订购数据
        self.button_data_sale = QtWidgets.QPushButton(self.centralwidget)
        self.button_data_sale.setGeometry(QtCore.QRect(40, 190, 221, 51))
        self.button_data_sale.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_data_sale.setObjectName("button_data_sale")
        self.button_data_sale.clicked.connect(self.Load_data_sale)
        self.button_data_sale.setToolTip('上期订购数据字段：\n"CUST_ID" (零售户ID)\n"ITEM_ID" (品规ID)\n"QTY_NEED" (需求量/条)\n"QTY_SOLD" (订购成交量/条)')

        # 4.上传品规信息
        self.button_data_item = QtWidgets.QPushButton(self.centralwidget)
        self.button_data_item.setGeometry(QtCore.QRect(40, 270, 221, 51))
        self.button_data_item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_data_item.setObjectName("button_data_item")
        self.button_data_item.clicked.connect(self.Load_data_item)
        self.button_data_item.setToolTip('品规信息字段：\n"品规名"\n"品规ID"\n"本期产能" (条)\n"批发价格" (元/条)')

        # 5.上传零售户信息
        self.button_data_cust = QtWidgets.QPushButton(self.centralwidget)
        self.button_data_cust.setGeometry(QtCore.QRect(40, 350, 221, 51))
        self.button_data_cust.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_data_cust.setObjectName("button_data_cust")
        self.button_data_cust.clicked.connect(self.Load_data_cust)
        self.button_data_cust.setToolTip('零售户信息字段：\n"客户ID"\n"档位" (1~30数字)')
        

        # 6.生成本期销量目标
        self.button_calc_sold_obj = QtWidgets.QPushButton(self.centralwidget)
        self.button_calc_sold_obj.setGeometry(QtCore.QRect(310, 660, 221, 51))
        self.button_calc_sold_obj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_calc_sold_obj.setObjectName("button_calc_sold_obj")
        self.button_calc_sold_obj.clicked.connect(self.Calc_sold_obj)

        # 7.调整销量目标
        self.button_ajust_sold_obj = QtWidgets.QPushButton(self.centralwidget)
        self.button_ajust_sold_obj.setGeometry(QtCore.QRect(560, 660, 221, 51))
        self.button_ajust_sold_obj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_ajust_sold_obj.setObjectName("button_ajust_sold_obj")
        self.button_ajust_sold_obj.clicked.connect(self.Obj_adjust)

        # 8.生成本期投放策略
        self.button_calc_strategy = QtWidgets.QPushButton(self.centralwidget)
        self.button_calc_strategy.setGeometry(QtCore.QRect(1060, 660, 201, 51))
        self.button_calc_strategy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_calc_strategy.setObjectName("button_calc_strategy")
        self.button_calc_strategy.clicked.connect(self.Calc_strategy)
        
        # 表格预览区
        self.sold_tableView = QtWidgets.QTableView(self.centralwidget)
        self.sold_tableView.setGeometry(QtCore.QRect(310, 30, 951, 601))
        self.sold_tableView.setObjectName("sold_tableView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1318, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 菜单栏：参数调整self.doc
        self.doc = QtWidgets.QAction(MainWindow)
        self.doc.setObjectName("doc")
        self.doc.triggered.connect(self.OpenHelp)

        # 菜单栏：帮助文档self.para
        self.para = QtWidgets.QAction(MainWindow)
        self.para.setObjectName("para")
        self.para.triggered.connect(self.ModiPara)

        self.menu.addAction(self.doc)
        self.menu.addAction(self.para)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " 智投放V1.2"))

        self.input_sold_obj.setPlaceholderText(_translate("MainWindow", "1.输入销量目标（箱）"))
        self.input_price_obj.setPlaceholderText(_translate("MainWindow", "2.输入结构目标（元/箱）"))

        self.button_data_sale.setText(_translate("MainWindow", "3.上传上期订购数据"))
        self.button_data_item.setText(_translate("MainWindow", "4.上传品规信息"))
        self.button_data_cust.setText(_translate("MainWindow", "5.上传零售户信息"))

        self.button_calc_sold_obj.setText(_translate("MainWindow", "6.生成本期销量目标"))
        self.button_ajust_sold_obj.setText(_translate("MainWindow", "7.调整销量目标"))
        self.button_calc_strategy.setText(_translate("MainWindow", "8.生成本期投放策略"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.doc.setText(_translate("MainWindow", "帮助文档"))
        self.para.setText(_translate("MainWindow", "参数调整"))

    def table_show(self, data):
        '''输入pd.DataFrame显示在sold_tableView'''
        model = PandasModel(data)
        self.sold_tableView.setModel(model)

    def OpenHelp(self):
        '''菜单栏：帮助文档'''
        webbrowser.open('https://docs.qq.com/doc/DYm9GVWd5d0ZnY092')

    def ModiPara(self):
        '''
        菜单栏：参数调整
        '''
        self.para_window = Ui_Para()
        self.para_window.show()


    def Load_data_sale(self):
        '''
        3.上传上期订购数据
        数据框赋值到 self.data_sale
        '''
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "上传上期销量数据", "",'''All Files (*);;
                            Microsoft Excel 工作表 (*.xlsx);;
                            Microsoft Excel 97-2003 工作表 (*.xls);;
                            CSV 逗号分隔文件 (*.csv)''', options=options)[0]
        if fileName:
            try: # pandas读入数据容易出错,防止闪退
                self.data_sale = pd.read_excel(fileName)
                self.table_show(self.data_sale)
            except xlrd.XLRDError: # 如果输入的是csv
                self.data_sale = pd.read_csv(fileName)
                self.table_show(self.data_sale)
            except: 
                QtWidgets.QMessageBox.critical(self, '错误', '上传数据失败')

    def Load_data_item(self):
        '''
        4.上传品规数据
        数据框赋值到 self.data_item
        '''
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "上传上期销量数据", "",'''All Files (*);;
                            Microsoft Excel 工作表 (*.xlsx);;
                            Microsoft Excel 97-2003 工作表 (*.xls);;
                            CSV 逗号分隔文件 (*.csv)''', options=options)[0]
        if fileName:
            try: # pandas读入数据容易出错,防止闪退
                self.data_item = pd.read_excel(fileName)
                self.table_show(self.data_item)
            except xlrd.XLRDError: # 如果输入的是csv
                self.data_item = pd.read_csv(fileName)
                self.table_show(self.data_item)
            except: 
                QtWidgets.QMessageBox.critical(self, '错误', '上传数据失败')

    def Load_data_cust(self):
        '''
        5.上传零售户数据
        数据框赋值到 self.data_cust
        '''
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "上传上期销量数据", "",'''All Files (*);;
                            Microsoft Excel 工作表 (*.xlsx);;
                            Microsoft Excel 97-2003 工作表 (*.xls);;
                            CSV 逗号分隔文件 (*.csv)''', options=options)[0]
        if fileName:
            try: # pandas读入数据容易出错,防止闪退
                self.data_cust = pd.read_excel(fileName)
                self.table_show(self.data_cust)
            except xlrd.XLRDError: # 如果输入的是csv
                self.data_cust = pd.read_csv(fileName)
                self.table_show(self.data_cust)
            except: 
                QtWidgets.QMessageBox.critical(self, '错误', '上传数据失败')

    def Calc_sold_obj(self):
        '''
        6.生成本期销量目标
        self.sold_target: np.array in int dtype
        '''
        try:
            value_sold_obj = int(self.input_sold_obj.text())
            value_price_obj = float(self.input_price_obj.text())

            # 在self.data_item中求得
            self.data_item['上期销量'] = 0
            for i in self.data_item.index:
                item_ID = self.data_item.loc[i, '品规ID']
                qty_sale = self.data_sale[self.data_sale['ITEM_ID'] == item_ID]['QTY_SOLD'].sum()
                self.data_item.loc[i, '上期销量'] = qty_sale
            
            solu = Solution(para)
            self.sold_target = solu.stage_one(self.data_item, value_sold_obj, value_price_obj)   # 一阶段的解int array
            self.data_item['本期销量目标'] = pd.Series(self.sold_target, dtype='int') # 读入的self.data_item中增加列
            self.table_show(self.data_item) 

            # 弹窗评估目标分解结果
            target = self.sold_target.sum()/250
            target_d = (target-value_sold_obj)/value_sold_obj
            price = (self.sold_target * self.data_item['批发价格'].values * 250).sum()/self.sold_target.sum()
            price_d = (price-value_price_obj)/value_price_obj
            QtWidgets.QMessageBox.information(self, '提示', '此目标分解下：\n销量目标为 %.2f 箱，与输入偏差为 %.2f\n结构目标为 %.2f 元/箱，与输入偏差为 %.2f'%(target, target_d, price, price_d))

        except: # 计算出错不会闪退，只是没反应
            return

    def Obj_adjust(self):
        '''
        7.调整本期销量目标
        '''
        QtWidgets.QMessageBox.information(self, '提示', '此功能属于智能化投放部分，尚在开发，敬请期待')

    def Calc_strategy(self):
        '''
        8.生成本期投放策略
        点击调用二级窗口类
        '''
        # 创建一个QWidget对象作为子窗口,并设为类属性防止被销毁闪退
        self.sub_window = QtWidgets.QWidget()

        # 二级窗口类也需要赋值到主窗口类属性
        self.ui2 = Ui_Form()
        
        # 若未计算Calc_sold_obj()，也不会闪退，只是没反应
        try:
        # 传递到二级窗口类的数据
        # 销量目标 value_sold_obj
        # 结构目标 value_price_obj
        # 订购数据 data_sale: CUST_ID ITEM_ID QTY_NEED	QTY_SOLD 品规名 本期产能 批发价格 档位
        # 品规数据 data_item: 品规名 品规ID 本期产能 批发价格 上期销量 本期销量目标
        # 零售户数据 data_cust: 客户ID 档位
            self.ui2.value_sold_obj = float(self.input_sold_obj.text())
            self.ui2.value_price_obj = float(self.input_price_obj.text())
            self.ui2.data_sale = pd.merge(self.data_sale, self.data_item, left_on='ITEM_ID', right_on='品规ID', how='right').drop('品规ID',axis=1) # 由品规ID引入名称、价格
            self.ui2.data_sale = pd.merge(self.ui2.data_sale, self.data_cust, left_on='CUST_ID', right_on='客户ID', how='left').drop('客户ID',axis=1) # 由客户ID引入档位
            self.ui2.data_item = self.data_item
            self.ui2.data_cust = self.data_cust
        except:
            return

        # 二级窗口类布局
        self.ui2.setupUi(self.sub_window)             
        self.sub_window.show() 



class Ui_Para(QtWidgets.QWidget):
    '''参数调节窗口类'''
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self): 
        # 软件关闭，重新打开参数调节窗口：全局变量从json中读入
        # 软件保持开启，重新打开参数调节窗口：全局变量在Ensure函数中已修改
        self.setObjectName("Para")
        self.resize(805, 550)
        if getattr(sys, 'frozen', False):
            root = os.path.dirname(sys.executable)
        else:
            root = QtCore.QFileInfo(__file__).absolutePath() # __file__是文件名字符串
        self.setWindowIcon(QtGui.QIcon(root+'/fav.ico'))

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 251, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 231, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 251, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 261, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 261, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(30, 410, 531, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(30, 340, 531, 21))
        self.label_8.setObjectName("label_8")

        self.delta_sold = QtWidgets.QDoubleSpinBox(self)
        self.delta_sold.setGeometry(QtCore.QRect(310, 30, 101, 41))
        self.delta_sold.setMaximum(1.0)
        self.delta_sold.setSingleStep(0.01)
        self.delta_sold.setProperty("value", para['delta_sold'])
        self.delta_sold.setObjectName("delta_sold")
 
        self.o1 = QtWidgets.QDoubleSpinBox(self)
        self.o1.setGeometry(QtCore.QRect(310, 150, 101, 41))
        self.o1.setMaximum(5.0)
        self.o1.setSingleStep(0.1)
        self.o1.setProperty("value", para['slym_o'][0])
        self.o1.setObjectName("o1")

        self.o2 = QtWidgets.QDoubleSpinBox(self)
        self.o2.setGeometry(QtCore.QRect(430, 150, 101, 41))
        self.o2.setMaximum(5.0)
        self.o2.setSingleStep(0.1)
        self.o2.setProperty("value", para['slym_o'][1])
        self.o2.setObjectName("o2")

        self.o3 = QtWidgets.QDoubleSpinBox(self)
        self.o3.setGeometry(QtCore.QRect(550, 150, 101, 41))
        self.o3.setMaximum(5.0)
        self.o3.setSingleStep(0.1)
        self.o3.setProperty("value", para['slym_o'][2])
        self.o3.setObjectName("o3")

        self.o4 = QtWidgets.QDoubleSpinBox(self)
        self.o4.setGeometry(QtCore.QRect(670, 150, 101, 41))
        self.o4.setMaximum(5.0)
        self.o4.setSingleStep(0.1)
        self.o4.setProperty("value", para['slym_o'][3])
        self.o4.setObjectName("o4")

        self.w1 = QtWidgets.QDoubleSpinBox(self)
        self.w1.setGeometry(QtCore.QRect(310, 90, 101, 41))
        self.w1.setSingleStep(0.1)
        self.w1.setMinimum(-10.0)
        self.w1.setMaximum(10.0)
        self.w1.setProperty("value", para['slym_w'][0])
        self.w1.setObjectName("w1")

        self.w2 = QtWidgets.QDoubleSpinBox(self)
        self.w2.setGeometry(QtCore.QRect(430, 90, 101, 41))
        self.w2.setSingleStep(0.1)
        self.w2.setMinimum(-10.0)
        self.w2.setMaximum(10.0)
        self.w2.setProperty("value", para['slym_w'][1])
        self.w2.setObjectName("w2")

        self.w3 = QtWidgets.QDoubleSpinBox(self)
        self.w3.setGeometry(QtCore.QRect(550, 90, 101, 41))
        self.w3.setSingleStep(0.1)
        self.w3.setMinimum(-10.0)
        self.w3.setMaximum(10.0)
        self.w3.setProperty("value", para['slym_w'][2])
        self.w3.setObjectName("w3")

        self.w4 = QtWidgets.QDoubleSpinBox(self)
        self.w4.setGeometry(QtCore.QRect(670, 90, 101, 41))
        self.w4.setSingleStep(0.1)
        self.w4.setMinimum(-10.0)
        self.w4.setMaximum(10.0)
        self.w4.setProperty("value", para['slym_w'][3])
        self.w4.setObjectName("w4")

        self.thre1 = QtWidgets.QDoubleSpinBox(self)
        self.thre1.setGeometry(QtCore.QRect(310, 210, 101, 41))
        self.thre1.setSingleStep(0.01)
        self.thre1.setMinimum(-10.0)
        self.thre1.setMaximum(10.0)
        self.thre1.setProperty("value", para['thre'][0])
        self.thre1.setObjectName("thre1")

        self.thre2 = QtWidgets.QDoubleSpinBox(self)
        self.thre2.setGeometry(QtCore.QRect(430, 210, 101, 41))
        self.thre2.setSingleStep(0.01)
        self.thre2.setMinimum(-10.0)
        self.thre2.setMaximum(10.0)
        self.thre2.setProperty("value", para['thre'][1])
        self.thre2.setObjectName("thre2")

        self.beta = QtWidgets.QDoubleSpinBox(self)
        self.beta.setGeometry(QtCore.QRect(310, 270, 101, 41))
        self.beta.setSingleStep(0.01)
        self.beta.setMinimum(0)
        self.beta.setMaximum(5)
        self.beta.setProperty("value", para['beta'])
        self.beta.setObjectName("beta")

        # 档位优先级
        self.alpha = QtWidgets.QDoubleSpinBox(self)
        self.alpha.setGeometry(QtCore.QRect(310, 330, 101, 41))
        self.alpha.setSingleStep(0.01)
        self.alpha.setMinimum(-5)
        self.alpha.setMaximum(5)
        self.alpha.setProperty("value", para['alpha'])
        self.alpha.setObjectName("alpha")

        self.recover = QtWidgets.QPushButton(self)
        self.recover.setGeometry(QtCore.QRect(670, 470, 101, 41))
        self.recover.setObjectName("recover")
        self.recover.clicked.connect(self.Recover) # 按钮：恢复默认

        self.ensure = QtWidgets.QPushButton(self)
        self.ensure.setGeometry(QtCore.QRect(430, 470, 101, 41))
        self.ensure.setObjectName("ensure")
        self.ensure.clicked.connect(self.Ensure) # 按钮：确认修改

        self.cancel = QtWidgets.QPushButton(self)
        self.cancel.setGeometry(QtCore.QRect(550, 470, 101, 41))
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.close) # 按钮：取消

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Para", "参数调整"))

        self.label_2.setText(_translate("Para", "允许销售额浮动范围"))
        self.label_3.setText(_translate("Para", "三率一面权重"))
        self.label_4.setText(_translate("Para", "三率一面理想目标"))
        self.label_5.setText(_translate("Para", "饱和-不饱和阈值"))
        self.label_6.setText(_translate("Para", "市场反馈评分最小调节单位"))
        self.label_7.setText(_translate("Para", "【注】三率一面按“订足面、订足率、订单满足率、订购率”排序"))
        self.label_8.setText(_translate("Para", "档位优先级程度"))
        self.recover.setText(_translate("Para", "复位"))
        self.ensure.setText(_translate("Para", "确认修改"))
        self.cancel.setText(_translate("Para", "取消"))

    def Recover(self):
        '''按钮：恢复默认'''
        self.delta_sold.setProperty("value", 0.01)
        self.w1.setProperty("value", 3)
        self.w2.setProperty("value", 3)
        self.w3.setProperty("value", 1)
        self.w4.setProperty("value", 0.1)
        self.o1.setProperty("value", 0.5)
        self.o2.setProperty("value", 0.5)
        self.o3.setProperty("value", 0.8)
        self.o4.setProperty("value", 0.5)
        self.thre1.setProperty("value", -0.8)
        self.thre2.setProperty("value", 0.8)
        self.beta.setProperty("value", 0.3)
        self.alpha.setProperty("value", 0.12)
     
    def Ensure(self):
        '''
        按钮：确认修改
        修改全局变量para
        并将全局变量para输出到json中
        '''
        global para # 本函数内使用的是全局变量

        para['delta_sold'] = self.delta_sold.value()
        para['slym_w'] = [self.w1.value(), self.w2.value(), self.w3.value(), self.w4.value()]
        para['slym_o'] = [self.o1.value(), self.o2.value(), self.o3.value(), self.o4.value()]
        para['thre'] = [self.thre1.value(), self.thre2.value()]
        para['beta'] = self.beta.value()
        para['alpha'] = self.alpha.value()

        with open('parameter.json', 'w') as f:
            f.write(json.dumps(para))
        QtWidgets.QMessageBox.information(self, '提示', '参数修改成功！') 


class Ui_Form(QtWidgets.QWidget):
    '''二级窗口类'''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1439, 744)
        if getattr(sys, 'frozen', False):
            root = os.path.dirname(sys.executable)
        else:
            root = QtCore.QFileInfo(__file__).absolutePath() # __file__是文件名字符串
        Form.setWindowIcon(QtGui.QIcon(root+'/fav.ico'))

        # 1.上传上期投放策略
        self.button_pre_stra = QtWidgets.QPushButton(Form)
        self.button_pre_stra.setGeometry(QtCore.QRect(40, 660, 181, 51))
        self.button_pre_stra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_pre_stra.setObjectName("button_pre_stra")
        self.button_pre_stra.clicked.connect(self.Load_pre_stra) 
        self.button_pre_stra.setToolTip('上期投放策略字段：\n"商品名称","30档","29档"...,"1档"')

        # 2.生成投放策略
        self.button_calc_strategy = QtWidgets.QPushButton(Form)
        self.button_calc_strategy.setGeometry(QtCore.QRect(250, 660, 181, 51))
        self.button_calc_strategy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_calc_strategy.setObjectName("button_calc_strategy")
        self.button_calc_strategy.clicked.connect(self.Calc_strategy)

        # 3.导出CSV文件
        self.output_csv = QtWidgets.QPushButton(Form)
        self.output_csv.setGeometry(QtCore.QRect(1210, 660, 181, 51))
        self.output_csv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.output_csv.setObjectName("output_csv")
        self.output_csv.clicked.connect(self.Output_csv)

        # "计算进度"文字
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(510, 660, 71, 51))
        self.label.setObjectName("label")

        # 进度条
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(620, 670, 481, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        # 显示投放策略
        self.strategy_tableView = QtWidgets.QTableView(Form)
        self.strategy_tableView.setGeometry(QtCore.QRect(40, 30, 1351, 591))
        self.strategy_tableView.setObjectName("strategy_tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " 自动化常规投放"))

        self.button_pre_stra.setText(_translate("Form", "1.上传上期投放策略"))
        self.button_calc_strategy.setText(_translate("Form", "2.生成本期投放策略"))
        self.output_csv.setText(_translate("Form", "3.导出表格文件"))
        self.label.setText(_translate("Form", "计算进度"))

    def Table_show(self, data):
        '''输入pd.DataFrame显示在strategy_tableView'''
        model = PandasModel(data)
        self.strategy_tableView.setModel(model)

    def Load_pre_stra(self):
        '''
        二级窗口中上传三率一面数据
        数据框赋值到self.data_pre_stra
        '''
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, "上传三率一面数据", "",'''所有文件 (*);;
                                            Microsoft Excel 工作表 (*.xlsx);;Microsoft Excel 97-2003 工作表 (*.xls)''', options=options)[0]
        if fileName:
            try: # pandas读入数据容易出错,防止闪退.待实现：弹窗报错、读入xlsx
                self.data_pre_stra = pd.read_excel(fileName)
                self.Table_show(self.data_pre_stra)
            except: 
                QtWidgets.QMessageBox.critical(self, '错误', '数据上传失败')
    
    def Calc_strategy(self):
        '''
        根据三率一面数据self.slym_data
            本期销售目标数据self.sold_obj_data (itemid, sold_target)
        计算投放策略self.strategy : pd.DataFrame in shape of (item_number, 30+2)
        并显示在strategy_tableView中
        '''
        solu = Solution(para)

        try:
            self.strategy = solu.stage_two(self, self.data_pre_stra, self.data_sale, self.data_item, self.data_cust)
            self.Table_show(self.strategy[0]) # self.strategy[0]: 本期策略表 形状和上期策略表一致

            pred_sale = self.strategy[1] # self.strategy[1]: 预期总销量（条）
            pred_price = self.strategy[2] # self.strategy[2]：预期结构（元/箱）
            pred_sale_change = (pred_sale-self.value_sold_obj)/self.value_sold_obj
            pred_price_change = (pred_price-self.value_price_obj)/self.value_price_obj

            QtWidgets.QMessageBox.information(self, '提示', '此投放策略下:\n预期销量为 %.2f 箱，与目标偏差为 %.2f\n预期结构为 %.2f 元/箱，与目标偏差为 %.2f'%(pred_sale,pred_sale_change,pred_price,pred_price_change))
        except:
            QtWidgets.QMessageBox.critical(self, '错误', '策略计算失败')


    def Output_csv(self):
        '''导出self.strategy'''
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,"输出投放策略文件",".xlsx","""Microsoft Excel 工作表 (*.xlsx);;
                                                            Microsoft Excel 97-2003 工作表 (*.xls);;所有文件 (*)""", options=options)
        if fileName:
            try: 
                self.strategy[0].to_excel(fileName)
                QtWidgets.QMessageBox.information(self, '提示', '投放策略导出成功！')
            except: 
                QtWidgets.QMessageBox.critical(self, '错误', '投放策略导出失败')


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







class Solution(object):
    '''模型求解类'''
    def __init__(self, para):
        '''超参数传入'''
        # 一阶段模型参数
        self.delta_sold = para['delta_sold'] # 允许销售额的浮动范围 0.01

        # 二阶段模型参数
        self.slym_weight = para['slym_w'] # 三率一面的权重向量 [3,3,1,0.1]
        self.slym_object = para['slym_o'] # 三率一面的调整目标 [0.5,0.5,0.8,0.5]
        self.thre = para['thre'] # 不饱和、饱和的阈值 [-0.8, 0.8]
        self.beta = para['beta'] # 市场反馈评分最小调节单位，每单位策略对评分的影响大小 0.3
        self.alpha = para['alpha'] # 档位优先程度 0.12 score默认扣除0.12 * (30-dw) 档位越高score越大,越容易不饱和

    def stage_one(self, arg_source, sold_obj, price_obj):
        '''
        一阶段求解：本期销量目标
        输入
            arg_source 包括'批发价格'(单条价)，'上期销量'，'本期产能'
            sold_obj
            price_obj
        输出
            np.array int
        '''

        price = arg_source['批发价格'].values * 250
        sold = arg_source['上期销量'].values 
        cap = arg_source['本期产能'].values
        I = price.size

        var = [i for i in map(lambda x: 'x(' + str(x) + ')', list(range(arg_source.shape[0])))] # ['x(0)', 'x(1)', ...]
        c = price/(250*sold_obj*price_obj) # (Σc_i*x_i)^2中的c
        lp = '' # lp文件内容

        # p1: 一次项 x1 x2 x3 ...
        p1 = ''
        for i in range(len(cap)):
            p1 += ' - %s x(%s)'%((2*I*price/(250*sold_obj*price_obj) + 2/sold)[i], i)

        # p2: 二次项 x1^2 x2^2 ... (已经乘2)
        p2 = ''
        for i in range(len(cap)):
            p2 += ' + %s x(%s)^2'%((2 * I * c**2 + 2/(sold**2))[i], i)

        # p3: 交叉二次项 x1x2 x1x3 ... (已经乘2)
        p3 = ''
        for i in range(len(cap)):
            for j in range(i+1, len(cap)):
                p3 += ' + %s x(%s) * x(%s)'%(4*I*c[i]*c[j],i,j)

        lp += ('Minimize\n obj:' + p1 + ' +[' + p2 + p3 + ']/2\n')

        # 约束条件

        # p4: Σx_i
        p4 = ''
        for i in range(len(cap)):
            p4 += ' + %s x(%s)'%(1/250, i)

        lp += '\nSubject To\n'
        lp += ' c1: %s >= %s \n'%(p4, (1-self.delta_sold)*sold_obj)
        lp += ' c2: %s <= %s \n'%(p4, (1+self.delta_sold)*sold_obj)
        for i in range(len(cap)):
            lp += ' c%s: x(%s) - Rgc%s = 0\n'%(3+i, i, i)
        lp += 'Bounds\n'
        for i in range(len(cap)): 
            lp += 'x(%s) Free\n'%i
        for i in range(len(cap)): 
            lp += ' 0 <= Rgc%s <= %s \n'%(i, cap[i])
        lp += 'General\n'
        for i in range(len(cap)): lp += ' %s'%(var[i])
        lp += '\nEnd'

        with open('write.lp', 'w') as f:
            f.write(lp)       
        
        # 读取LP文件并调用CPLEX求解
        my_prob = cplex.Cplex('write.lp')
        my_prob.solve()
        try:
            x = my_prob.solution.get_values() # 会将解重复一遍
            return np.array(x, dtype='int')[0:int(len(x)/2)]
        except:
            QtWidgets.QMessageBox.critical(QtWidgets.QWidget(), '错误', '模型无解：请调整销量或结构目标') # 无解时弹窗报错
            return np.array([0]*I)

    def stage_two(self, window, pre_stra, data_sale, data_item, data_cust):
        '''
        输入：
            window: 调用stage_two的窗口类，其中包括进度条
            pre_stra: 上期策略表 [商品名称 30档 29档 ...]
            data_sale: 订购数据 所有品规所有档位 [CUST_ID ITEM_ID QTY_NEED QTY_SOLD 品规名 本期产能 批发价格 档位]
            data_item: 品规信息 [品规名 品规ID 本期产能 批发价格 上期销量 本期销量目标]
            data_cust: 零售户信息 [客户ID 档位]
        输出：
            out_print:  本期策略表 形状和上期策略表一致
            pred_sale_sum: 预期总销量（箱）
            pred_price：预期结构（元/箱）
        '''
        out_print = pd.DataFrame(columns=pre_stra.columns)
        pred_sale_sum = 0
        pred_price = 0

        for ind in pre_stra.index:
            item_name = pre_stra.loc[ind, '商品名称']
            item_sale = data_sale[data_sale['品规名']==item_name]
            if item_sale.shape[0]==0: continue # 如果上期策略中的某品规在订购记录中没有数据
            max_need = []
            score = []
            strat = []

            for i in range(30):    
                dw = 30-i # dw由30~1
                cube = item_sale[item_sale['档位']==dw] # 某品规某档位上的订购数据,可能有空数据框即该档位对该品规没有需求
                num  = data_cust[data_cust['档位']==dw].shape[0]
                put  = pre_stra[pre_stra['商品名称']==item_name].values[0][i+1]
                # 该品规在30-1档上的最大需求list max_need
                if cube.shape[0]: max_need.append(cube['QTY_NEED'].max())
                else: max_need.append(0)
                score.append(self.cal_score(cube, dw, num, put))
                strat.append(put)

            sold_obj = data_item[data_item['品规名']==item_name]['本期销量目标'].values[0]
            sold_pre = data_item[data_item['品规名']==item_name]['上期销量'].values[0]
            sold_price = data_item[data_item['品规名']==item_name]['批发价格'].values[0]
            item_stra = self.single_strategy(item_name, item_sale, np.array(max_need), np.array(score), np.array(strat), sold_obj, sold_pre) 
            # item_stra: 该品规下期策略，预测的品规销量

            out_print.loc[ind,:] = item_stra[0]
            pred_sale_sum += item_stra[1] # 条
            pred_price += (item_stra[1]*sold_price) # 条*（元/条）

            print(item_stra[0], '上期销量',sold_pre, '销量目标',sold_obj, '完成目标',item_stra[1])

            prog = int(100*(ind+1)/pre_stra.shape[0])
            window.progressBar.setValue( prog )
            
        pred_sale_sum /= 250 # 箱
        pred_price /= pred_sale_sum # 元/箱
        
        return out_print, pred_sale_sum, pred_price

    def single_strategy(self, item_name, item_sale, max_need, score, strat, sold_obj, sold_pre): 
        '''
        单品规投放策略
        输入：
            item_name: 品规名称
            item_sale: 单个品规在30~1档上的订购数据明细
            max_need: 单个品规在30~1档上的最大需求向量 np.array
            score: 单个品规在30~1档上的不饱和度向量 np.array
            strat: 单个品规在30~1档上的上期策略向量 np.array
            sold_obj: 该品规在30~1档上的总销量目标(条)
            sold_pre: 该品规在30~1档上的上期总销量(条)
        输出：
            output: np.array [name, ID, 30'(+3), 29'(-1), ...] str
            sold_sim: 旧需求、新策略下完成的该品规总销量
        '''
        strategy = copy.copy(strat) # 浅拷贝,可变对象相当于传址调用,会改变原值
        sold_sim = copy.copy(sold_pre)


        # 需增加投放
        if sold_obj - sold_pre > 3: 

            # 扣掉过于饱和的档位
            # for i in range(0,30):
            #     while score[i] < self.thre[0]:
            #         if strategy[i] <= 0: break
            #         strategy[i] -= 1
            #         score[i] += self.beta
            # sold_sim = self.number(item_sale, strategy)

            # 在不饱和档位上增加投放
            while (sold_obj > sold_sim) and (strategy < max_need).any(): # 当所有策略都>=最大需求时，跳出
                t = np.where(score==score.max())[0][0]
                if strategy[t] < max_need[t]: # 策略比最大需求小的档位才增加策略
                    strategy[t] += 1
                    score[t] -= self.beta
                    sold_sim = self.number(item_sale, strategy)
                else:
                    score[t] -= 10000


        # 需减少投放,相等则不调整策略
        elif sold_obj - sold_pre < -3: 

            # 在过于不饱和的档位上增加投放
            for i in range(0,30):
                while score[i] > self.thre[1]:
                    strategy[i] += 1
                    score[i] -= self.beta
                    sold_sim = self.number(item_sale, strategy)

            # 在饱和的档位上减少投放
            while sold_obj < sold_sim: 
                t = np.where(score==score.min())[0][0]
                if strategy[t] > 0:
                    strategy[t] -= 1
                    score[t] += self.beta
                    sold_sim = self.number(item_sale, strategy)
                else:
                    score[t] += 10000

        print('上期',sold_pre, '目标',sold_obj, '完成',sold_sim)

        change = strategy - strat
        output = [str(x) for x in strategy]
        for i in range(30):
            if change[i] > 0:  output[i] += ' (+%s)'%change[i]
            elif change[i] < 0: output[i] += ' (%s)'%change[i]
        output = np.append(item_name, output) # 打印的内容 [name, ID, 30', 29', ...]

        return output,sold_sim

    def number(self, item_sale, stra):
        '''
        在某品规的订购明细中
        给定30-1档位策略向量 stra: list/np.array
        求在新策略下的总销量
        '''
        sold = 0
        for i in range(30):
            need = item_sale[item_sale['档位']==30-i]['QTY_NEED'].values
            strat = np.array([stra[i]]*need.size)
            sold += (need[need <= strat].sum() + strat[need > strat].sum())
        return sold
    
    def cal_score(self, cube, dw, num, put):
        '''
        根据某品规、某档位上的订购数据，计算不饱和度
        cube: CUST_ID,ITEM_ID,QTY_NEED,QTY_SOLD,品规名,本期产能,批发价格,档位. 可能会存在空数据框,即该档位在该品规上没有需求
        num: 该档位的总户数
        put: 该品规、该档位的上期投放策略. 可能会存在0,即该档位在该品规上没有投放
        dw: 档位
        '''
        if (cube.shape[0] == 0) or (put == 0): return -self.alpha*(30-dw)
        dzm = cube[cube['QTY_NEED']==cube['QTY_SOLD']].shape[0]/cube.shape[0]
        dzl = cube['QTY_SOLD'].sum()/(put*num)
        ddmz = cube['QTY_SOLD'].sum()/cube['QTY_NEED'].sum()
        dgl = cube.shape[0]/num 
        score = self.slym_weight[0]*(self.slym_object[0]-dzm)+self.slym_weight[1]*(dzl-self.slym_object[1])+self.slym_weight[2]*(self.slym_object[2]-ddmz)+self.slym_weight[3]*(dgl-self.slym_object[3])-self.alpha*(30-dw)
        return score



class Ui_About(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 293)
        if getattr(sys, 'frozen', False):
            root = os.path.dirname(sys.executable)
        else:
            root = QtCore.QFileInfo(__file__).absolutePath() # __file__是文件名字符串
        Form.setWindowIcon(QtGui.QIcon(root+'/fav.ico'))
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 481, 251))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">卷烟智投放系统</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本信息：V1.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">帮助文档：https://docs.qq.com/doc/DYm9GVWd5d0ZnY092</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">开发方：四川大学商学院数智泉团队</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">联系我们：qiancheng1948@outlook.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版权归属：广西中烟工业责任有限公司</p></body></html>"))


# -------------------------------------
app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
ui = Ui_Start()                         # ui是你创建的ui类的实例化对象
ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication