'''
@Description: 
@Version: 
@Autor: qc
@Date: 2020-04-26 18:56:35
@LastEditors: qc
@LastEditTime: 2020-05-06 14:02:21
'''
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

buildOptions = dict(includes = 'atexit',
                    include_files = ['fav.ico','V1.1-Introduction.png','parameter.json','demo_data/step1.xlsx','demo_data/step2.xlsx'])

# packages =  ['sys', 'copy', 'numpy', 'pandas', 'cplex',
                          #      'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'], 

import sys
base = None
if sys.platform == 'win32': 
    base = 'Win32GUI' # none表示cmd控制台而不是GUI


executables = [
    Executable(
        script = 'smartPut.py',
        base = base,
        icon = 'fav.ico',
        targetName = 'smartPut'
        )
]

setup(name='SmartPut-V1.1',
      version = '1.1',
      description = '卷烟智投放系统',
      options = dict(build_exe = buildOptions),
      executables = executables)
