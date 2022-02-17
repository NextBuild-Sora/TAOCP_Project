# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:27:45 2020

@author: Mi-PRO-2020
"""

# --- 数据的CSV文件存取 --- 
# --- 读入--

'''
    CSV (Comma‐Separated Value, 逗号分隔值) .
    CSV是一种常见的文件格式，用来存储批量数据.
    
    局限性：
        CSV只能有效存储一维和二维数组 。
        np.savetxt() np.loadtxt()只能有效存取一维和二维数组。
  ----------------------------------------
  
  np.loadtxt(frame, dtype=np.float, delimiter=None， unpack=False)
  
  • frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件 
  • dtype : 数据类型，可选 • delimiter : 分割字符串，默认是任何空格 
  • unpack: 如果True，读入属性将分别写入不同变量

'''

import numpy as np

b = np.loadtxt( 'a.csv', delimiter=',' )
print ( "默认：", b )

b = np.loadtxt( 'a.csv', dtype = np.int, delimiter = ',' )
print ( "int类型：", b )




