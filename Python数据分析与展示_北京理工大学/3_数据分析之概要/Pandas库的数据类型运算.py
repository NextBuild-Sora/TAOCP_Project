
# --- Pandas库的数据类型运算 --- #

#******************************************************
'''
      算术运算法则：
            算术运算根据行列索引，补齐后运算，运算默认产生浮点数
                  补齐时缺项填充NaN (空值)
            二维和一维、一维和零维间为广播运算
                 采用+ ‐ * /符号进行的二元运算产生新的对象
'''
#******************************************************

import pandas as pd
import numpy as np

a = pd.DataFrame(np.arange(12).reshape(3,4))
print("a数据： ")
print (a)
print()

b = pd.DataFrame( np.arange(20).reshape(4,5) )
print("b数据: ")
print (b)
print()

#自动补齐，缺项补NaN:
啊 =  a + b
print("a+b运算： ")
print (啊)

print()
print( "a*b运算： " )
print ( a*b )
print()

'''
    .add(d, **argws) 类型间加法运算，可选参数
    .sub(d, **argws) 类型间减法运算，可选参数
    .mul(d, **argws) 类型间乘法运算，可选参数
    .div(d, **argws) 类型间除法运算，可选参数
'''

# fill_value参数替代NaN,替代后参与运算：
print("加法运算： ")
print ( b.add( a, fill_value = 100 ) )
print("乘法运算： ")
print ( a.mul(b, fill_value = 0 ) )

print()

# 不同维度间为广播运算，一维Series默认在轴1参与运算： 
c = pd.Series(np.arange(4))
print("c数组： ")
print ( c )
print()
print("c减10： ")
print( c - 10 )
print()
print("b减c: ")
print(  b - c )


