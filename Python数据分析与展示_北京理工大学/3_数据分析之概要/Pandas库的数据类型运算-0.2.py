
# --- Pandas库的数据类型运算 --- #
# --0.2--

#******************************************************
'''
      比较运算法则：
            比较运算只能比较相同索引的元素，不进行补齐 
                二维和一维、一维和零维间为广播运算
            采用> < >= <= == !=等符号进行的二元运算产生布尔对象
'''
#******************************************************


import pandas as pd
import numpy as np

a = pd.DataFrame( np.arange(12).reshape(3,4) )
print("a数列： ")
print( a )

print()

d = pd.DataFrame( np.arange(12, 0, -1).reshape(3,4) )
print("d数列： ")
print( d )

print()

# 同纬度运算，尺寸一致：
print( a>d )
print()
print( a == d )
print()

c = pd.Series(np.arange(4))
print("c数列： ")
print(c)
print()

# 不同维度运算，默认在1轴：
print(a > c)
print()
print(c > 0)


