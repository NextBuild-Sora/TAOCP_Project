# -*- Pandas库小测 -*-

import pandas as pd

d = pd.Series( range(20) )  #Series类型由一组数据及与之相关的数据索引组成
 
print ( d )
print()

print ("计算前N项累加和：")
print (  d.cumsum() )



'''
    ---- Pandas库的理解 ---- 
        两个数据类型：Series, DataFrame 
    基于上述数据类型的各类操作：
        基本操作、运算操作、特征类操作、关联类操作
    扩展数据类型
    关注数据的应用表达 
    数据与索引间关系
'''
