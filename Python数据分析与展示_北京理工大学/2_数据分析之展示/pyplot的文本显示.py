
# --- pyplot的文本显示 --- #


import numpy as np 
import matplotlib.pyplot as plt 

a = np.arange( 0.0, 5.0, 0.02 )
plt.plot ( a, np.cos( 2*np.pi*a ), 'r--' )

# x轴文本标签：
plt.xlabel( '横轴：时间', fontproperties = 'simhei', fontsize = 15, color = 'green' )

# y轴文本标签：
plt.ylabel( '纵轴：时间', fontproperties =  'simhei', fontsize = 15 )

# 对图形整体增加文本标签：
plt.title( r'正弦波实例 $ y = cos(2 \pi x) $ ', fontproperties = 'simhei', fontsize = 15 )

# 在任意位置增加文本：
plt.text( 2, 1, r'$ \mu = 100 $', fontsize = 15 )


plt.axis( [-1, 6, -2, 2] )
plt.grid(True)  #网格。
plt.show()

