# ---NumPy的随机数函数--- #
# 0.1版

"""
    NumPy的random子库 ：
        np.random.*：
            np.random.rand()
            np.random.randn() 
            np.random.randint()
    
"""
'''
    rand(d0,d1,..,dn) : 根据d0‐dn创建随机数数组，浮点数，[0,1)，均匀分布。
    randn(d0,d1,..,dn): 根据d0‐dn创建随机数数组，标准正态分布。
    randint(low[,high,shape]) ：根据shape创建随机整数或整数数组，范围是[low, high)。
    seed(s)：随机数种子，s是给定的种子值 。                                           

'''
#*************************************************************************#

import numpy as np

a = np.random.rand(3, 4, 5)
print ( " 随机数组（浮点数），均匀分布： ", a )
print()

sn = np.random.randn(3, 4, 5)
print ("随机数数组（标准正态分布）: ")
print ( "    ", sn )
print()

b = np.random.randint(100, 200, (3,4) )
print ("随机整数：")
print( b )

print()

c = np.random.seed(10)
print ( "给定随机数种子值：10", c )
c = np.random.randint(100, 200, (3,4))
print ( "种子值是10的:",  c )

