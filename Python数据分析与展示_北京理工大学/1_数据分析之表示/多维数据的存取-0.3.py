# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:57:21 2020

@author: Mi-PRO-2020
"""


# --- 多维数据的存取 --- #
#--0.3--
# NnmPy的便捷文件存取

'''
    存储：np.save(fname, array) 或 np.savez(fname, array)
        • fname : 文件名，以.npy为扩展名，压缩扩展名为.npz 
        • array : 数组变量
    
    读入：np.load(fname) 
        • fname : 文件名，以.npy为扩展名，压缩扩展名为.npz    

'''

import numpy as np


a = np.arange(100).reshape(5, 10, 2)
np.save("a3.npy", a )   #二进制格式
#print ( a )

b = np.load("a3.npy")   #还原整数格式
print ( b )

