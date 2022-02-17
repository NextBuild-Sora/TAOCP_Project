# ---NumPy的统计数函数--- #

'''
    --- NumPy直接提供的统计类函数 
    np.*
        np.std() 
        np.var() 
        np.average()
---------------------------------
        sum(a, axis=None) ：根据给定轴axis计算数组a相关元素之和，axis整数或元组 。
        mean(a, axis=None) ：根据给定轴axis计算数组a相关元素的期望，axis整数或元组。
        verage(a,axis=None,weights=None) 根据给定轴axis计算数组a相关元素的加权平均值 。
        std(a, axis=None)：根据给定轴axis计算数组a相关元素的标准差。
        var(a, axis=None)： 根据给定轴axis计算数组a相关元素的方差。
        
'''
#**********************************************************************#


import numpy as np


a = np.arange(15).reshape(3,5)
print ("随机数组：", a)
print()
print ("求和（总和）：", np.sum(a))
print()

print ( "期望值（平均值）：", np.mean(a, axis=1) )
print()

print ( "期望值：", np.mean(a, axis= 0 ) )  # axis=0: 最外层维度。
print()

print ( "加权平均值：", np.average(a, axis = 0,weights = [10,5,1] ) )
print()

print ( "标准差：", np.std(a) )
print()

print ( "方差：", np.var(a) )









