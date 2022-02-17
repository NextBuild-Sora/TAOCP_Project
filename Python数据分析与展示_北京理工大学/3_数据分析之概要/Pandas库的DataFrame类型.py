
# -*- Pandas库的DataFrame类型 -*- #


#*******************************************************
'''
    DataFrame类型由共用相同索引的一组列组成.
    
       DataFrame是一个表格型的数据类型，每列值类型可以不同 .
     DataFrame既有行索引、也有列索引.
   DataFrame常用于表达二维数据，但可以表达多维数据 . 


    DataFrame类型可以由如下类型创建：
    • 二维ndarray对象
    • 由一维ndarray、列表、字典、元组或Series构成的字典
    • Series类型
    • 其他的DataFrame类型
    
    
    DataFrame是二维带“标签”数组。
    DataFrame基本操作类似Series，依据行列索引。
'''
#******************************************************


import pandas as pd
import numpy as np

# -- 二维ndarray对象创建：
d = pd.DataFrame( np.arange(10).reshape(2,5) )

print ("二维ndarray对象创建：  ")
print ( d )

print()
#——————————————————————————————————————————————————————


# -- 从一维ndarray对象字典创建：
dt = {'one':pd.Series([1,2,3], index = ['a', 'b', 'd']), 
      'two':pd.Series([9, 8, 7, 6], index = ['a', 'b', 'c', 'd'])}

d = pd.DataFrame(dt)

print("一维ndarray对象字典创建：")
print ( d )
print()
#数据根据行列索引自动补齐：
print ("自动对齐：")
print ( pd.DataFrame(dt, index=['b', 'c', 'd'], columns = ['Two', 'Three'] ))

print()
#————————————————————————————————————————————————————————


# -- 从列表类型的字典创建：
d1 = {'第一列':[1,2,3,4], 'two':[9,8,7,6] }
d = pd.DataFrame( d1, index = ['a', 'b', 'c', 'd'])

print ("列表类型的字典： ")
print ( d )
print()

# 2016年7月部分大中城市新建住宅价格指数--
d1 = {'城市':['北京', '上海', '广州', '深圳', '沈阳'], 
      '环比':[101.5, 101.2, 101.3, 102.0, 100.1], 
      '同比':[120.7, 127.3, 119.4, 140.9, 101.4], 
      '定基':[121.4, 127.8, 120.0, 145.5, 101.6]}

d = pd.DataFrame( d1, index = ['c1', 'c2', 'c3', 'c4', 'c5'] )

print("住宅价格指数： ")
print ( d )     
print()

print ( "d索引：", d.index ) #索引。
print()
print ( "d的", d.columns )   #列索引。
print()
print ( "d的值：", d.values )  #值。
print()
print ( d['同比'] )   # ’同比‘ 一列。
print()
# print ( d.ix['c2'] )  # ix函数功能已被官方移除。使用loc函数功能作为替代。
print ( d.loc['c2'] )   # 使用loc函数功能作为替代。


print ( d['同比']['c2'] )     # ‘同比’一列，‘c2’一行。
print()






