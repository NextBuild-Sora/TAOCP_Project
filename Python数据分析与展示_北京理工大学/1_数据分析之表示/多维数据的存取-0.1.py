# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:57:21 2020

@author: Mi-PRO-2020
"""


# --- 多维数据的存取 --- #

'''
    任意维度数据如何存取呢？
        
    a.tofile(frame, sep='', format='%s')
        • frame : 文件、字符串 。
        • sep: 数据分割字符串，如果是空串，写入文件为二进制 。
        • format : 写入数据的格式。


'''

import numpy as np

#存储（写入）：
a1 = np.arange(100).reshape(5,10,2)
a1.tofile("b.dat", sep=",", format = '%d')  #整数

a2 = np.arange(100).reshape( 5, 10, 2 )     #二进制
a2.tofile( "b0.dat", format = '%d' )


#读取（读入）：
'''
    np.fromfile(frame, dtype=float, count=‐1, sep='')
        • frame : 文件、字符串 
        • dtype : 读取的数据类型 
        • count : 读入元素个数，‐1表示读入整个文件 
        • sep: 数据分割字符串，如果是空串，写入文件为二进制
'''
