

# -*- Pandas库：数据的基本统计分析 -*-

#-----------------------------------------------
'''
    ----- 基本的统计分析函数 -----

                ---- 适用于Series和DataFrame类型 ----
        .sum() : 计算数据的总和，按0轴计算，下同
        .count() : 非NaN值的数量
        .mean() .median() 计算数据的算术平均值、算术中位数
        .var() .std() : 计算数据的方差、标准差
        .min() .max(): 计算数据的最小值、最大值

               --- 适用于Series类型 ---
        .argmin() .argmax() 计算数据最大值、最小值所在位置的索引位置（自动索引） 
        .idxmin() .idxmax() 计算数据最大值、最小值所在位置的索引（自定义索引）

               -- 适用于Series和DataFrame类型 --
        .describe() 针对0轴（各列）的统计汇总

'''
#-----------------------------------------------


import pandas as pd 


a = pd.Series([9,8,7,6], index = ['a', 'b', 'c', 'd'])

print ( a.desribe() )
print()

print( type(a.describe) )
print()

print (a.describe()['count'])
print()

print(a.describe()['max'])
print()

import numpy as np 

b = pd.DataFrame(np.arange(20).reshape(4,5), index = ['a', 'c' ,'d', 'b'])
b1 = b.descibe()
b2 = b.descibe().ix['max']
b3 = b.descibe()[2]

print ( 
    b1 '\n', 
    b2 '\n', 
    b3 '\n' 
    )




