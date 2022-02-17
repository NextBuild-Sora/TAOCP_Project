# -*- Pandas库小测 -*-

import pandas as pd
import numpy as np 

#*************************************************#
# --- Series类型由一组数据及与之相关的数据索引组成。
'''

    Series类型可以由如下类型创建： 
    • Python列表 
    • 标量值 
    • Python字典 
    • ndarray 
    • 其他函数
'''
#*************************************************#


# d = pd.Series( range(20) )  

# 列表创建：
a = pd.Series( [9,8,7,6] )

print ("列表创建：")

print ( a )
print()

b = pd.Series( [9,8,7,6],  ['a', 'b', 'c', 'd'] )    #第二个参数：自定义索引，可以省略index=
print ( "自定义索引：")
print ( b )

print()

b1 = pd.Series( [9,8,7,6], index =  ['a', 'b', 'c', 'd'] )    #第二个参数：自定义索引，可以省略index=
print (b1)

print()
#————————————————————————————————————————————————————————————————————

# 从标量值创建：
s = pd.Series(25, index = ['a', 'b', 'c'])  #不能省略index.

print("标量值创建：")
print (s)
print ( pd.Series(15, ['a','a']) )  #运行正常，发现可以省略index.
print()
#——————————————————————————————————————————————————————————————

# 从字典类型创建：
d = pd.Series({'a':9, 'b':8, 'c':7})

print("字典创建：")
print (d)

print ( pd.Series({'a':1, 'b':2, 'c':3}, index = ['c', 'a', 'b', 'e']) )    #index从字典中进行选择操作

print()
#————————————————————————————————————————————————————————————

#ndarray类型创建：
n = pd.Series( np.arange(5) )

print("ndarray类型创建：")
print (n)

m = pd.Series( np.arange(5), index=np.arange( 9,4,  -1 ) )
print ( m )

