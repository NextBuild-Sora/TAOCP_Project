# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:27:45 2020

@author: Mi-PRO-2020
"""

# --- 数据的的CSV文件存取 --- 
# --- 存储--

'''
    CSV (Comma‐Separated Value, 逗号分隔值) .
    CSV是一种常见的文件格式，用来存储批量数据.
  ----------------------------------------
  
  np.savetxt(frame, array, fmt='%.18e', delimiter=None).
  • frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件. 
  • array : 存入文件的数组 .
  • fmt : 写入文件的格式，例如：%d %.2f %.18e .
  • delimiter : 分割字符串，默认是任何空格.

'''

import numpy as np

a = np.arange( 100 ).reshape( 5, 20 )
np.savetxt( 'a.csv', a, fmt = '%d', delimiter = ',' )

a1 = a
np.savetxt( 'a1.csv', a1, fmt = '%.1f', delimiter= '/' )

