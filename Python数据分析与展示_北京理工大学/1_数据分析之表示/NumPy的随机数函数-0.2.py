# ---NumPy的随机数函数--- #
# 0.2版

"""
    NumPy的random子库 ：
        np.random.*：
            np.random.rand()
            np.random.randn() 
            np.random.randint()
    
"""
'''
---- shuffle(a) : 根据数组a的第1轴进行随排列，改变数组x.
    permutation(a) : 根据数组a的第1轴产生一个新的乱序数组，不改变数组x.
    choice(a[,size,replace,p]) : 从一维数组a中以概率p抽取元素，形成size形状新数组 replace表示是否可以重用元素，默认为False.
   
'''


import numpy as np

a = np.random.randint(100, 200, (3,4))
print ("随机整数：", a)
print()

#print( "洗牌：", np.random.shuffle(a) )   # 此方法不能
np.random.shuffle(a)
print ( "洗牌：", a )
print()


b = np.random.randint(100, 200, (3,4))
print ( " b 随机数组：", b)

print ("交换（产生一个新的乱序数组）", np.random.permutation(b))  # 行进行交换
#print ( "交换（产生一个新的乱序数组）：", b)   #此方法不能

print ( " b 随机数组( 不改变) ：", b )
print()

c = np.random.randint(100, 200, (8, ))
print (" c 随机数组：", c)

print ( "选择：", np.random.choice(c, (3,2)) )

# print ( np.random.choice(c, (3,2)), p=c/np.sum(c) )     
# IPyton控制台上运行正常，不知为何这里报错？？？！！！
# 括号符有问题。

# np.random.choice(c,(3,2), p = c/np.sum(c))
print (" p概率随机：", np.random.choice(c,(3,2),p = c/np.sum(c)) )







