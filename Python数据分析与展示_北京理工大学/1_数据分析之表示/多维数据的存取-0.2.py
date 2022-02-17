# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:57:21 2020

@author: Mi-PRO-2020
"""


# --- 多维数据的存取 --- #


import numpy as np



#读取（读入）：
'''
    np.fromfile(frame, dtype=float, count=‐1, sep='')
        • frame : 文件、字符串 
        • dtype : 读取的数据类型 
        • count : 读入元素个数，‐1表示读入整个文件 
        • sep: 数据分割字符串，如果是空串，写入文件为二进制
'''

a = np.arange(100).reshape( 5, 10,2 )
a.tofile( "b.dat", sep = ',', format='%d' )
c = np.fromfile( 'b.dat', dtype = np.int, sep = ',' )
print ( " a默认 ： ", c )

c = np.fromfile( 'b.dat', dtype = np.int, sep=',' ).reshape( 5, 10 ,2 )
print ( " reshape函数： ", c )


a1 = np.arange(100).reshape(5, 10, 2)
a1.tofile( "b.dat", format= '%d' )
c = np.fromfile( "b.dat", dtype = np.int).reshape(5, 10, 2) 
print ( "  a1 ：", c )

