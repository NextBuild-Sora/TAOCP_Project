

# --- pyplot的plot（）函数 --- #
# --0.1版-- 

#**********************************************************#

'''
    plt.plot(x, y, format_string, **kwargs)

        ∙ x : X轴数据，列表或数组，可选 
        ∙ y: Y轴数据，列表或数组
        ∙ format_string: 控制曲线的格式字符串，可选 
        ∙ **kwargs: 第二组或更多(x,y,format_string) 

    ---当绘制多条曲线时，各条曲线的x不能省略

'''
#**********************************************************#



import matplotlib.pyplot as plt
import numpy as np 

a = np.arange(10)
plt.plot( a, a*1.5, a,a*2.5, a,a*3.5, a,a*4.5 )
plt.show()

