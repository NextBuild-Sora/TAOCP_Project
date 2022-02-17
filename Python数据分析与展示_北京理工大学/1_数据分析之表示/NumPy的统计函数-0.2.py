# ---NumPy的统计数函数--- #
# -0.2-

'''
    --- NumPy直接提供的统计类函数 
    np.*
        np.std() 
        np.var() 
        np.average()
---------------------------------
         min(a) max(a) ：计算数组a中元素的最小值、最大值 。
         argmin(a) argmax(a) ：计算数组a中元素最小值、最大值的降一维后下标 。
         unravel_index(index, shape) ：根据shape将一维下标index转换成多维下标 。
         ptp(a)  ：计算数组a中元素最大值与最小值的差 。
         median(a) ：计算数组a中元素的中位数（中值）。

'''
#**********************************************************************#


import numpy as np


b = np.arange(15,0,-1).reshape(3,5)
print ( "随机数组：", b )
print()

print ( "最大值：", np.max(b))
print() 

print ( "最大值（降一维后下标）：", np.argmax(b))   #扁平化后的下标。
print()

print ( "重塑成多维下标：", np.unravel_index(np.argmax(b), b.shape ))     #重塑成多维下标。
print()

print ( "最大值与最小值的差：", np.ptp(b))
print()

print ( "中位数（中值）：", np.median(b))









