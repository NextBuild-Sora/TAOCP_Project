
# --- pyplot的文本显示 --- #
# --0.2版 -- 

import numpy as np 
import matplotlib.pyplot as plt 

a = np.arange( 0.0, 5.0, 0.02 )
plt.plot ( a, np.cos( 2*np.pi*a ), 'r--' )

plt.xlabel( '横轴：时间', fontproperties = 'simhei', fontsize = 12, color = 'green' )
plt.ylabel( '纵轴：时间', fontproperties =  'simhei', fontsize = 12 )
plt.title( r'正弦波实例 $ y = cos(2 \pi x) $ ', fontproperties = 'simhei', fontsize = 15 )

# 在图形中增加带箭头的注解：
plt.annotate ( r'$ \mu = 100 $', xy = (2, 1), xytext = (3, 1.5), 
            arrowprops = dict (facecolor = 'black', shrink = 0.1, width = 2 ) )


plt.axis( [-1, 6, -2, 2] )
plt.grid(True)  #网格。
plt.show()


#********************************************************************#
#    plt.annotate(s, xy=arrow_crd, xytext=text_crd, arrowprops=dict)
#********************************************************************#


