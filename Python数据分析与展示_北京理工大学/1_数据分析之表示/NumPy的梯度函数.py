# ---NumPy的梯度函数--- #

#***********************************************************************#
'''
  np.gradient(f) 
    计算数组f中元素的梯度，当f为多维时，返回每个维度梯度
    梯度：连续值之间的变化率，即斜率 
    XY坐标轴连续三个X坐标对应的Y轴值：a, b, c，其中，b的梯度是： (c‐a)/2
'''
#**********************************************************************#


import numpy as np


a = np.random.randint(0, 20, (5))
print (a)
print (np.gradient(a))

print()


b = np.random.randint(0,20,(5))
print (b)
print (np.gradient(b))

print()

c = np.random.randint(0,50,(3,5))
print (c)
print(np.gradient(c))












