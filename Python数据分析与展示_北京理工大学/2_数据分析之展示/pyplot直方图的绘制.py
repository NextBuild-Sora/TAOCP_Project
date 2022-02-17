# -*- pyplot饼图的绘制 -*-
# --  --


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
mu, sigma = 100, 20     #均值和标准差
a = np.random.normal( mu, sigma, size = 100 )

plt.hist( a, 20, normed = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75 )
plt.title('Histogram')

plt.show( )



