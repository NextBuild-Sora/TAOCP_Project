
# --*-- Pandas库:数据的累计统计分析 --*-- #


#-----------------------------------------------
'''

    适用于Series和DataFrame类型，累计计算
        .cumsum(): 依次给出前1、2、…、n个数的和
        .cumprod(): 依次给出前1、2、…、n个数的积
        .cummax(): 依次给出前1、2、…、n个数的最大值
        .cummin(): 依次给出前1、2、…、n个数的最小值

'''
#-------------------------------------------------



import pandas as pd
import numpy as np


b = pd.DataFrame( np.arange(20).reshape(4,5), index = ['一', '二', '三', '四'] )

print("b数列： " '\n', b )
print()

b1 = b.cumsum()
b2 = b.cumprod()
b3 = b.cummin()
b4 = b.cummax()
print ( b1 ,'\n', 
        b2 ,'\n', 
        b3 , '\n', 
        b4 , '\n' )


#_____________________________________________________
'''
    ---适用于Series和DataFrame类型，滚动计算（窗口计算）
    .rolling(w).sum(): 依次计算相邻w个元素的和
    .rolling(w).mean(): 依次计算相邻w个元素的算术平均值
    .rolling(w).var(): 依次计算相邻w个元素的方差
    .rolling(w).std(): 依次计算相邻w个元素的标准差
    .rolling(w).min() .max() : 依次计算相邻w个元素的最小值和最大值

'''
#_______________________________________________________


print ( "相邻2个元素和： " '\n', b.rolling(2).sum() )
print()

print ( "相邻3个元素和： " '\n', b.rolling(3).sum() )

