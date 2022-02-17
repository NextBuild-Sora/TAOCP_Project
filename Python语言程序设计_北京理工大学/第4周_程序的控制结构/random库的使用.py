
 # ------------------------ random库的使用 -------------------------------#
 
'''
    random库：主要用于生成随计数；使用随机数的Python标准库。
            
              伪随机数：采用梅森旋转算法生成的（伪）随机序列中元素。

                  1、基本随机数函数：
                      
                      seed()：初始化给定的随机数种子，默认为当前系统时间.
                      
                      random(): 生成一个[a, b]之间的整数.


                 2、扩展随机数函数：
                      
                      randint(): 生成一个[m, n)之间以k为步长的随机整数.
                      
                      getrandbits(): 生成一个k比特长的随机整数.
                      
                      uniform(): 生成一个[a, b]之间的随机小数.
                      
                      randrange():生成一个[m, n)之间以k为步长的随机整数.
                      
                      choice(): 从序列seq (列表) 中随机选择一个元素.
                      
                      shuffle(): 将序列seq中元素随机排列，返回打乱后的序列.
                      
'''

# ------------------------------------------------------------------------#


import random

random.seed(10)     # 产生种子10对应的序列。
q = random.random()     # 生成一个 0.0 与 1.0 之间的随机小数。
print ('0与1之间：',q)

q1 = random.random()
print ('0,1:',q1)

random.seed(10)     # 产生种子10对应的序列。
q2 = random.random()
print ('0与1之间：',q2)

w = random.randint(10,100)
print ('a,b 之间整数：',w)

w1 = random.randrange(10,100,10)
print ('a,b 之间以K为步长的随机整数：',w1)

w3 = random.getrandbits(19)
print ('K比特长：',w3)

w4 = random.uniform(9,34)
print ('随机小数：',w4)

w5= random.randrange( 1,34,5 )
print ('w1:',w5)

w6 = random.choice( [ 1,23,4,5,6,88 ] )
print ('序列中：',w6)

s = ( [ 1,23,4,5,6,88 ] ); random.shuffle(s)
print ('随机打乱序列：',s)


