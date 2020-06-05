# -*- coding: utf-8 -*-

import sys
import copy
import numpy as np 
import pandas as pd
import cplex
from scipy.optimize import minimize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox

class Ui_Start(QtWidgets.QMainWindow):
    '''主窗口类'''
    def setupUi(self, Start):
        Start.setObjectName("MainWindow")
        root = QtCore.QFileInfo(__file__).absolutePath()
        Start.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
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
        self.action_3.triggered.connect(QApplication.quit)

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

    def retranslateUi(self, Start):
        _translate = QtCore.QCoreApplication.translate
        Start.setWindowTitle(_translate("MainWindow", " 智投放V1.0"))
        self.fun1.setText(_translate("MainWindow", "自动化 常规投放"))
        self.fun2.setText(_translate("MainWindow", "智能化 常规投放"))
        self.fun3.setText(_translate("MainWindow", "智能化 新品选点"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#043193;\">欢迎使用 智投放系统！</span></p></body></html>"))
        self.fun3_2.setText(_translate("MainWindow", "智能化 补货替代"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action_2.setText(_translate("MainWindow", "关于"))
        self.action_3.setText(_translate("MainWindow", "退出"))

    def auto_put(self):
        '''点击调用一级窗口类'''
        self.sub_window = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self.sub_window)
        self.sub_window.show()

    def smart_put(self):
        '''智能化投放仍在开发'''
        QMessageBox.information(self, '提示', '此功能属于智能化投放部分，尚在开发，敬请期待')

    def about(self):
        '''关于我们'''
        self.about_window = QtWidgets.QWidget()
        self.ui3 = Ui_About()
        self.ui3.setupUi(self.about_window)
        self.about_window.show()

class Ui_MainWindow(QtWidgets.QMainWindow):
    '''一级窗口类'''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 790)
        root = QtCore.QFileInfo(__file__).absolutePath()
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 1.输入销量目标（条）
        self.sold_obj = QtWidgets.QLineEdit(self.centralwidget)
        self.sold_obj.setGeometry(QtCore.QRect(20, 30, 221, 51))
        self.sold_obj.setInputMask("")
        self.sold_obj.setText("")
        self.sold_obj.setMaxLength(32767)
        self.sold_obj.setAlignment(QtCore.Qt.AlignCenter)
        self.sold_obj.setObjectName("sold_obj")

        # 2.输入结构目标（元/箱）
        self.price_obj = QtWidgets.QLineEdit(self.centralwidget)
        self.price_obj.setGeometry(QtCore.QRect(20, 110, 221, 51))
        self.price_obj.setText("")
        self.price_obj.setAlignment(QtCore.Qt.AlignCenter)
        self.price_obj.setObjectName("price_obj")

        # 3.上传上期销量数据
        self.upload_sold = QtWidgets.QPushButton(self.centralwidget)
        self.upload_sold.setGeometry(QtCore.QRect(20, 190, 221, 51))
        self.upload_sold.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_sold.setObjectName("upload_sold")
        self.upload_sold.clicked.connect(self.Load_sold)

        # 4.生成本期销量目标
        self.calc_sold_obj = QtWidgets.QPushButton(self.centralwidget)
        self.calc_sold_obj.setGeometry(QtCore.QRect(20, 580, 221, 51))
        self.calc_sold_obj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calc_sold_obj.setObjectName("calc_sold_obj")
        self.calc_sold_obj.clicked.connect(self.Calc_sold_obj)

        # 5.附加：销量目标调整（二阶段内容）
        self.obj_adjust = QtWidgets.QPushButton(self.centralwidget)
        self.obj_adjust.setGeometry(QtCore.QRect(800, 650, 201, 51))
        self.obj_adjust.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.obj_adjust.setObjectName("obj_adjust")
        self.obj_adjust.clicked.connect(self.Obj_adjust)

        # 6.生成本期投放策略
        self.calc_strategy = QtWidgets.QPushButton(self.centralwidget)
        self.calc_strategy.setGeometry(QtCore.QRect(1020, 650, 201, 51))
        self.calc_strategy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calc_strategy.setObjectName("calc_strategy")
        self.calc_strategy.clicked.connect(self.Calc_strategy)

        # 表格预览
        self.sold_tableView = QtWidgets.QTableView(self.centralwidget)
        self.sold_tableView.setGeometry(QtCore.QRect(265, 31, 951, 601))
        self.sold_tableView.setObjectName("sold_tableView")

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
        self.actionPara = QtWidgets.QAction(MainWindow)
        self.actionPara.setObjectName("actionPara")

        self.menu.addSeparator()
        self.menu.addAction(self.actionPara)
        self.menu.addAction(self.actionHelp)
        self.menubar.addAction(self.menu.menuAction())

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " 自动化常规投放"))
        self.sold_obj.setPlaceholderText(_translate("MainWindow", "1.输入销量目标（条）"))
        self.price_obj.setPlaceholderText(_translate("MainWindow", "2.输入结构目标（元/箱）"))
        self.upload_sold.setText(_translate("MainWindow", "3.上传上期销量数据"))
        self.calc_sold_obj.setText(_translate("MainWindow", "4.生成本期销量目标"))
        self.obj_adjust.setText(_translate("MainWindow", "5.调整销量目标"))
        self.calc_strategy.setText(_translate("MainWindow", "6.生成本期投放策略"))

        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionHelp.setText(_translate("MainWindow", "帮助文档"))
        self.actionPara.setText(_translate("MainWindow", "参数调整"))


    def Load_sold(self):
        '''
        3.上传上期销量数据
        数据框赋值到self.sold_data
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getOpenFileName(None, "上传上期销量数据", "",'''All Files (*);;
                                                        Comma Separated Values Files (*.csv)''', options=options)[0]
        if fileName:
            try: # pandas读入数据容易出错,防止闪退.待实现：弹窗报错
                self.sold_data = pd.read_excel(fileName, dtype={'品规ID':str})
                self.table_show(self.sold_data)
            except: pass

    def Calc_sold_obj(self):
        '''
        4.生成本期销量目标
        self.sold_target: np.array in int dtype
        '''
        try:
            Sold_obj = int(self.sold_obj.text())
            Price_obj = float(self.price_obj.text())

            # self.sold_data中有缺失值，用mean填补，并弹出警告或报错

            if self.sold_data.loc[:,['品规名','单箱价格','品规ID']].isnull().sum().sum() > 0:
                QMessageBox.critical(self, '错误', '品规名，单箱价格或品规ID有缺失，请重新上传数据')
                return # 重新上传数据

            if (self.sold_data['上期销售量'].isnull().sum()>0) or (self.sold_data['产能'].isnull().sum()>0):
                self.sold_data['上期销售量'].fillna(self.sold_data['上期销售量'].mean(), inplace=True)
                self.sold_data['产能'].fillna(10e6, inplace=True)   
                QMessageBox.warning(self, '警告', '上期销量或产能有缺失，已智能补全')
            
            solu = Solution()
            self.sold_target = solu.stage_one(self.sold_data, Sold_obj, Price_obj)   # 一阶段的解int array
            self.sold_data['本期销量目标'] = pd.Series(self.sold_target, dtype='int') # 读入的sold_data中增加列
            self.table_show(self.sold_data)

        except: # 计算出错不会闪退，只是没反应
            return

    def table_show(self, data):
        '''输入pd.DataFrame显示在sold_tableView'''
        model = PandasModel(data)
        self.sold_tableView.setModel(model)

    def Calc_strategy(self):
        '''
        5.生成本期投放策略
        点击调用二级窗口类
        '''
        # 创建一个QWidget对象作为子窗口,并设为类属性防止被销毁闪退
        self.sub_window = QWidget()
        # 二级窗口类也需要赋值到主窗口类属性
        self.ui2 = Ui_Form()
        # 本期销售目标需要以pd.DataFrame(item, itemid, sold_target)的形式赋值给二级窗口实例
        
        try: # 若未计算sold_target，也不会闪退，只是没反应
            self.ui2.sold_obj_data = pd.DataFrame({'item':self.sold_data['品规名'].values, 'itemid':self.sold_data['品规ID'].values, 'sold_target':self.sold_target}) 
        except:
            return
        # 二级窗口类布局
        self.ui2.setupUi(self.sub_window)             
        self.sub_window.show() 

    def Obj_adjust(self):
        QMessageBox.information(self, '提示', '此功能属于智能化投放部分，尚在开发，敬请期待')


class Ui_Form(QWidget):
    '''二级窗口类'''
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1439, 744)
        root = QtCore.QFileInfo(__file__).absolutePath()
        Form.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))

        # 1.上传三率一面数据
        self.upload_slym = QtWidgets.QPushButton(Form)
        self.upload_slym.setGeometry(QtCore.QRect(40, 660, 181, 51))
        self.upload_slym.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_slym.setObjectName("upload_slym")
        self.upload_slym.clicked.connect(self.Load_slym) 

        # 2.生成投放策略
        self.calc_strategy = QtWidgets.QPushButton(Form)
        self.calc_strategy.setGeometry(QtCore.QRect(250, 660, 181, 51))
        self.calc_strategy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calc_strategy.setObjectName("calc_strategy")
        self.calc_strategy.clicked.connect(self.Calc_strategy)

        # 显示投放策略
        self.strategy_tableView = QtWidgets.QTableView(Form)
        self.strategy_tableView.setGeometry(QtCore.QRect(40, 30, 1351, 591))
        self.strategy_tableView.setObjectName("strategy_tableView")

        # 导出CSV文件
        self.output_csv = QtWidgets.QPushButton(Form)
        self.output_csv.setGeometry(QtCore.QRect(1210, 660, 181, 51))
        self.output_csv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.output_csv.setObjectName("output_csv")
        self.output_csv.clicked.connect(self.Output_csv)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " 自动化常规投放"))
        self.output_csv.setText(_translate("Form", "导出表格文件"))
        self.upload_slym.setText(_translate("Form", "1.上传三率一面数据"))
        self.calc_strategy.setText(_translate("Form", "2.生成投放策略"))

    def Load_slym(self):
        '''
        二级窗口中上传三率一面数据
        数据框赋值到self.slym_data
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getOpenFileName(None, "上传三率一面数据", "",'''所有文件 (*);;
                                                        CSV(逗号分隔) (*.csv)''', options=options)[0]
        if fileName:
            try: # pandas读入数据容易出错,防止闪退.待实现：弹窗报错、读入xlsx
                self.slym_data = pd.read_excel(fileName, dtype={'品规ID':str})
                QMessageBox.information(self, '提示', '数据上传成功！')
            except: 
                QMessageBox.critical(self, '错误', '数据上传失败')
    

    def Calc_strategy(self):
        '''
        根据三率一面数据self.slym_data
            本期销售目标数据self.sold_obj_data (itemid, sold_target)
        计算投放策略self.strategy : pd.DataFrame in shape of (item_number, 30+2)
        并显示在strategy_tableView中
        '''
        solu = Solution()
        try:
            self.strategy = solu.stage_two(self.slym_data, self.sold_obj_data)
            self.Table_show(self.strategy)
        except:
            QMessageBox.critical(self, '错误', '策略计算失败')
    
    def Table_show(self, data):
        '''输入pd.DataFrame显示在strategy_tableView'''
        model = PandasModel(data)
        self.strategy_tableView.setModel(model)

    def Output_csv(self):
        '''导出self.strategy'''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"输出投放策略文件",".xlxs","""所有文件 (*);;
                                                       Microsoft Excel 工作表 (*.xlsx)""", options=options)
        if fileName:
            try: 
                self.strategy.to_excel(fileName)
                QMessageBox.information(self, '提示', '投放策略导出成功！')
            except: 
                QMessageBox.critical(self, '错误', '投放策略导出失败')


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


class Solution(QWidget):
    '''模型求解类'''
    def stage_one(self, arg_source, sold_obj, price_obj):
        '''一阶段求解：return np.array in int dtype'''

        price = arg_source['单箱价格'].values
        sold = arg_source['上期销售量'].values 
        cap = arg_source['产能'].values
        C = 10000

        # 将模型写成LP文件
        var = [i for i in map(lambda x: 'x(' + str(x) + ')', list(range(arg_source.shape[0])))] # ['x(1)', 'x(2)', ...]
        price_sold_sum = ''
        for i in range(len(cap)):
            price_sold_sum += ' + %s x(%s)'%(price[i]/250, i)

        lp = "Minimize\n obj: "
        for i in range(len(cap)):
            lp += ' - %s x(%s)'%(500*sold_obj+2*C/sold[i], i)

        lp += '\n+ ['
        for i in range(len(cap)):
            lp += ' + %s x(%s)^2'%(2*C/sold[i]**2 + 2, i)
            for j in range(i+1, len(cap)):
                lp += ' + 4 x(%s) * x(%s)'%(i,j)
            lp += '\n'

        lp += ']/2\n'

        lp += ' + %s'%(sold_obj**2 + C*len(cap))

        lp += '\nSubject To\n'
        lp += ' c1: %s >= %s \n'%(price_sold_sum, 0.9*sold_obj*price_obj)
        lp += ' c2: %s <= %s \n'%(price_sold_sum, 1.1*sold_obj*price_obj)
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
            QMessageBox.critical(self, '错误', '模型无解：请调整销量或结构目标') # 无解时弹窗报错
            return np.array([0]*cap.size)


        

    def stage_two(self, slym_source, sold_obj):
        '''
        三率一面数据 slym_source: pd.DataFrame 
        销量目标数据 sold_obj: pd.DataFrame(item, itemid, sold_target)
        二阶段求解：return pd.DataFrame in shape of (品规数, 档位数)
        '''
        # 处理slym_source的缺失值
        slym_source = self.preprocess(slym_source)

        # 创建结果空数据框
        col = ['品规ID','品规名','三十档', '二十九档', '二十八档', '二十七档', '二十六档','二十五档','二十四档','二十三档',
                '二十二档','二十一档','二十档','十九档','十八档','十七档','十六档','十五档','十四档', '十三档',
                '十二档','十一档', '十档','九档','八档','七档','六档', '五档','四档','三档','二档','一档']
        strategy = pd.DataFrame(columns=col)

        # 计算各品规投放策略
        for i in range(sold_obj.shape[0]):
            # 以step1的item&itemid为基准遍历
            item_id = sold_obj['itemid'].values[i]
            item = sold_obj['item'].values[i]
            sold_aim = sold_obj['sold_target'].values[i]
            guide = self.get_guide(slym_source, item, item_id)
            strategy.loc[i,:] = self.single_strategy(guide, sold_aim)

        return strategy


    def preprocess(self, dt):
        '''
        处理数据框中的缺失值
        将各品规的档位按30到1排列
        返回处理后的数据框
        '''
        # 字符串“xx档”转为int
        name_list = ['三十档', '二十九档', '二十八档', '二十七档', '二十六档','二十五档','二十四档','二十三档','二十二档','二十一档',
          '二十档','十九档','十八档','十七档','十六档','十五档','十四档', '十三档','十二档','十一档', '十档','九档',
          '八档','七档','六档', '五档','四档','三档','二档','一档']

        t = 30
        for i in name_list: 
            dt['档位'] = dt['档位'].replace(i,t)
            t -= 1
        
        # 处理inf和Na
        null_rate = dt.isnull().sum().sum()/(dt.shape[0]*dt.shape[1]) # 三率一面数据中数据缺失率
        QMessageBox.warning(self, '警告','三率一面数据中缺失率为%.3f，已智能补全'%null_rate)
        dt = dt.replace(np.inf, 1) 
        dt['上期策略'].fillna(0, inplace=True) # '上期策略'的缺失用0填补,因为输出策略是据此调整的,用均值影响太大
        dt['上期策略'] = dt['上期策略'].astype(int) # '上期策略'需要转成int
        for column in list(dt.columns[dt.isnull().sum() > 0]):
            mean_val = dt[column].mean()
            dt[column].fillna(mean_val, inplace=True)

        # 将各品规的档位按30到1排列
        dt.sort_values(by=['品规ID','档位'],inplace=True,ascending=[True,False])  
        return dt     

    def get_guide(self, slym, item, itemid):
        '''
        @description: 由品规名、品规ID在预处理过的三率一面数据中得到该品规的三率一面、上期策略等指导数据（step2品规名的校验）
        @parameter: slym DataFrame; itemid np.int64
        @return: dict{三率一面,上期策略,品规名,上期订购总量,各组总户数} / NA (没有匹配到该品规的三率一面)
        '''
        # 由step1的'品规ID'筛选出该品规的三率一面数据框
        item_cube = slym[slym['品规ID'] == itemid]

        # 若在step2中未匹配到该品规ID则返回None
        if item_cube.shape[0] == 0:
            return {'strategy':None, 'item':item, 'itemid':itemid}

        # 该品规ID匹配到的不是30行，则弹窗报错
        if item_cube.shape[0] != 30:
            QMessageBox.critical(self, '错误','三率一面数据中【ID%s：%s】不足30档，请检查数据后重新上传'%(itemid,item))

        # step2中的 品规ID-品规名 校验，若有不符则弹窗警告
        item2 = item_cube['品规名'].values[0]
        if (item != item2) or (item_cube['品规名'].value_counts().size != 1):
            QMessageBox.warning(self, '警告','三率一面数据中品规名和ID不匹配：ID%s-%s'%(itemid, item2))


        strategy = list(item_cube['上期策略']) # 上期投放策略
        dzm = list(item_cube['订足面'])
        dzl = list(item_cube['订足率'])
        ddmz = list(item_cube['订单满足率'])
        dgl = list(item_cube['订购率'])
        dg = item_cube['订购量']               # 各档订购量
        aimnow = sum(dg)                      # 上期订购总量
        number = item_cube['总户数']           # 各组总户数

        return {'strategy':strategy, 
                'dzm':dzm, 'dzl':dzl,'ddmz':ddmz, 'dgl':dgl,
                'item':item, 'itemid':itemid, 
                'aimnow':aimnow, 'number':number}
    
    def single_strategy(self, guide, sold_obj): 
        '''
        单品规投放策略
        输入：品规ID,品规名
        输出：list [ID, name, 30', 29', ...]
        '''
        # 如果step1中的'品规ID'在step2中没有匹配，则返回None列表（保留品规名和ID）
        if guide['strategy'] == None:
            return [guide['item'], guide['itemid']] + [None]*30

        strategy = copy.copy(guide['strategy']) # 浅拷贝,否则相当于传址调用,会修改guide_data['strategy']
        obj = sold_obj - guide['aimnow']        #订购量待调整量
        number_c = list(round(guide['number']*guide['dgl'])) #实际订购户数

        imf = [] #品规信息量
        for i in range(0,30):
            t = np.log(2*(30-i))-2
            imf.append(t)
        w = [3,3,1,0.1] #三率一面的权重

        #计算得分
        score = []
        for i in range(0,30):
            temp = (w[0]*(0.5-guide['dzm'][i])+w[1]*(guide['dzl'][i]-0.5)
                    +w[2]*(0.8-guide['ddmz'][i])+w[3]*(guide['dgl'][i]-0.5))-0.12*i
            score.append(temp)
        mean = 1/30*sum(score)
        for i in range(0,30):
            score[i] = (score[i]-mean)*(1-0.02*i)

        if obj >= 0:
            delta = 1.25 * obj
            for i in range(0,30):
                while score[i] < -0.8:
                    if strategy[i] <= 0:
                        break
                    strategy[i] -= 1
                    delta += number_c[i]
                    score[i] += 0.3
            while delta > 0:
                t = score.index(max(score))
                strategy[t] += 1
                score[t] -= 0.3
                delta -= number_c[i]
        else:
            delta = 0.8 * obj
            for i in range(0,30):
                while score[i] > 0.8:
                    strategy[i] += 1
                    delta -= number_c[i]
                    score[i] -= 0.3
            n = 1
            while delta < 0 and n <= 30:
                n += 1
                t = score.index(min(score))
                if strategy[t] > 0:
                    strategy[t] -= 1
                    score[t] += 0.3
                    delta += number_c[i]
                else:
                    score[t] += 10000
        
        strategy.insert(0, guide['item'])    # 策略list前插三率一面数据中匹配到的品规名
        strategy.insert(0, guide['itemid'])  # 策略list前插传入的品规ID
        return strategy

class Ui_About(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 293)
        root = QtCore.QFileInfo(__file__).absolutePath()
        Form.setWindowIcon(QtGui.QIcon(root+'/icons/fav.ico'))
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_Start()                       # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication