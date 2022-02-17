# -*- Pandas库-Series类型的基本操作 -*-


#*************************************************#
# --- Series类型基本操作---
#
#    Series类型包括index和values两部分 .
#    Series类型的操作类似ndarray类型 .
#    Series类型的操作类似Python字典类型.
#
#*************************************************#


import pandas as pd
import numpy as np


b = pd.Series( [9,8,7,6], ['a', 'b', 'c', 'd'] )
print (b) 
print()
print ( b.index )   #获得索引.
print()
print ( b.values )  #获得数据（值）.
print()

#自动索引和自定义索引并存：
print ("自定义索引：", b['b'])
print ("自动索引：", b[1])
print()
#两套索引并存，但不能混用：
#print ( b[ ['c', 'd', 0 ] ] )  #运行出现异常。

print ( b[ ['c', 'd', 'a'] ] )

print()
print('--*--' * 20)

#*********************************************************
#
#    Series类型的操作类似ndarray类型：
#    • 索引方法相同，采用[].
#    • NumPy中运算和操作可用于Series类型.
#    • 可以通过自定义索引的列表进行切片.
#    • 可以通过自动索引进行切片，如果存在自定义索引，则一同被切片.
#
#*********************************************************
    
#切片：
print ("切片：")
print ( b[3] )   #一个元素切片，只输出值。
print ( b[:3] )  #使用索引切片，会保留索引（连同索引和值）输出。
print()

print ( b[b>b.median()] )   #比较关系进行索引：输出大于中位数的值。
print() 
print ( np.exp(b) )     # e的幂次方.

print()


#**********************************
#    • 通过自定义索引访问.
#    • 保留字in操作.
#    • 使用.get()方法.
#**********************************

print ( "自定义索引访问： ", b['b'] )

print ( "in判断：", 'c' in b )
print ( 0 in b )
print()
print ( b.get('f', 100) )   #若‘f’索引不存在，则返回第二个参数。

print()
print('--*--' * 20)


#对齐操作：Series类型在运算中会自动对齐不同索引的数据。
# 只对齐相同索引，不同索引返回空值。
a = pd.Series( [1,2,3], ['c', 'd', 'e'] )
c = pd.Series( [9,8,7,6],['a', 'b', 'c', 'd'] )

print ( "自动对齐：" )
print ( a + b )

print()

#Series对象和索引都可以有一个名字，存储在属性.name中:
print ( 'name属性' )
print (b.name)  #空值，没有名字。
print()
b.name = 'Series对象'
b.index.name = '索引列'
print ( b )

print()

print('--*--' * 20)
#*****************************
# Series类型的修改：Series对象可以随时修改并即刻生效。
#*****************************

e = pd.Series( [9,8,7,6,5], ['a', 'b', 'c', 'd', 'e'] )

print( "Series对象修改： " )
print()

e['a'] = 15     #修改索引的值.
e.name = "Series类型"     #赋予名字.

print( e )
print()

e.name = "新的 Series类型"
e['b', 'c'] = 20    #修改索引的值
print ( e )

print()


