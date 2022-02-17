# -*- pyplot饼图的绘制 -*-
# -- 0.2 --


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu, sigma = 100, 20     #均值和标准差
a = np.random.normal( mu, sigma, size = 100 )

# plt.hist( a, 40, normed = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75 )

plt.hist( a, 40, density = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75 )
# plt.hist() 第二个参数：bin,直方图的个数。

plt.title('Histogram')

plt.show( )



#################################################################################################
    # plt.hist( a, 40, normed = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75 ) 
    
    #--- AttributeError: 'Polygon' object has no property 'normed' 
    
    #    normed函数已被官方取消使用，最新的归一化用参数 density=true
#################################################################################################




