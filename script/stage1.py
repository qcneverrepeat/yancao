'''
@Description: 投放模型一阶段 整数规划
@Version: 
@Autor: sz & qc & bruce
@Date: 2020-01-01 19:34:22
@LastEditors  : qc
@LastEditTime : 2020-01-01 19:39:45
'''

import numpy as np 
import pandas as pd
from scipy.optimize import minimize
import tkinter as tk 
import tkinter.messagebox
import os

# 读取参数数据
arg_source = pd.read_csv('D:/jupyter_dir/yancao/data/step1.csv', sep='\t')

# 定义参数变量
price = arg_source['price'].values
sold = arg_source['sold'].values 
cap = arg_source['cap'].values
sold_obj = 2800
price_obj = 40000
C = 1

# 目标函数
obj = lambda x: ((sold_obj*250 - x.sum())**2)*C + (((x - sold)/sold)**2).sum()

# 约束条件
cons = []
cons.append({'type':'ineq', 'fun': lambda x: (x*price).sum() - sold_obj*price_obj*0.9})
cons.append({'type':'ineq', 'fun': lambda x: sold_obj*price_obj*1.1 - (x*price).sum()})
for i in range(sold.size):
    cons.append({'type':'ineq', 'fun': lambda x: x[i]})
    cons.append({'type':'ineq', 'fun': lambda x: cap[i] - x[i]})

# 求解
sold_next = sold
sol = minimize(obj, sold_next, method='TNC', constraints=cons)

# sol.x



#建立窗口windows
window = tk.Tk()
window.title('中烟自动化投放系统-2')
window.geometry('1060x720')  # 这里的乘是小x
# 前置欢迎语
l = tk.Label(window, text='欢迎来到单品规自动化投放系统！\n当前品规: '+guide_data['item'], bg='#CD7F32', font=('Arial', 20), width=50, height=3)
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# c = tk.Label(window, text='您选择的数量是：', font=('Arial', 20), width=50, height=3)
# c.place(x=280,y=200)
#输入文本框
word1 = tk.Label(window, text='请输入您想要投放的数量：（单位：/条）', font=('Arial', 16), width=40, height=2)
word1.place(x=320,y=150)
e2 = tk.Entry(window, text='     ',show=None, font=('Arial', 14))  # 显示成明文形式
e2.place(x=420,y=200)
# 计算按钮
b = tk.Button(window, text='确 定', font=('Arial', 15), width=10, height=1, command=hit_me)
b.place(x=470,y=240)

# # 数量选择尺度滑条，长度500字符，从1000开始3000结束，以100为刻度，精度为1，触发调用print_selection函数
# s = tk.Scale(window, label='拖动滑块选择数量', from_=1000, to=3000, orient=tk.HORIZONTAL, length=500, showvalue=0,tickinterval=500, resolution=100, command=print_selection)
# s.place(x=280,y=200)
#输出界面
var = tk.StringVar()
output = tk.Label(window, textvariable=var, bg='#CDCDCD', fg='#00009C', font=('Arial', 18), width=68, height=12)
output.place(x=60, y=320)
b2 = tk.Button(window, text='一键导出CSV文件', font=('Arial', 15), width=15, height=1, command=hit_save)
b2.place(x=800,y=670)
window.mainloop()