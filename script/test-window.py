'''
@Description: 预览ui文件
@Version: 
@Autor: qc
@Date: 2020-01-01 22:01:44
@LastEditors: qc
@LastEditTime: 2020-03-13 19:23:21
''' 

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

Form, Window = uic.loadUiType("D:/jupyter_dir/yancao/UI/window2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()