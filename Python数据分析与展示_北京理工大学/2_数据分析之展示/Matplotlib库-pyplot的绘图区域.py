# --- Matplotlib库-pyplot的绘图区域 --- #


import matplotlib.pyplot as plt 
import numpy as np 

def f(t):   #能量衰减函数
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)    #绘图区域:  能量衰减曲线
plt.plot(a, f(a))

plt.subplot(2,1,2)   #绘图区域：正玄曲线
plt.plot( a, np.cos( 2*np.pi*a ), 'r--' )
plt.show()





