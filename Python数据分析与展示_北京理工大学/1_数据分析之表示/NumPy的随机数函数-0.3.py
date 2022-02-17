# ---NumPy的随机数函数--- #
# 0.3版


#******************************************************************************#
"""
    NumPy的random子库 ：
        np.random.*：
            np.random.rand()
            np.random.randn() 
            np.random.randint()
    
"""
'''
---- uniform(low,high,size)： 产生具有均匀分布的数组,low起始值,high结束值,size形状 。
    normal(loc,scale,size)： 产生具有正态分布的数组,loc均值,scale标准差,size形状 。
    poisson(lam,size)：产生具有泊松分布的数组,lam随机事件发生率,size形状。
'''
#******************************************************************************#


import numpy as np

u = np.random.uniform(0,10, (3,4))
print (  "均匀分布的数组：", u)
print()

n = np.random.normal(10, 5, (3,4))
print ("正态分布 数组：", n)









