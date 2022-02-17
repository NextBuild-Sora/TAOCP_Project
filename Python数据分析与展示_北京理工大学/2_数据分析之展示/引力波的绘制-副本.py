
# -- 引力波的绘制 -- 
# 副本

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 

#——————————————————————————————————————————————————————————————————
# 产生时间序列：从配置文档中读取时间相关数据。
rate_h, hstrain = wavfile.read( r'H1_Strain.wav', 'rb' )
rate_l, lstrain = wavfile.read( r'L1_Strain.wav', 'rb' )
reftime, ref_H1 = np.genfromtxt( 'wf_template.txt' ).transpose() 

#———————————————————————————————————————————————————————————————————
#读取应变数据：
htime_interval = 1/rate_h
ltime_interval = 1/rate_l

htime_len = hstrain.shape[0]/rate_h
htime = np.arange( -htime_len/2, htime_len/2, htime_interval  )
ltime_len = lstrain.shape[0]/rate_l
ltime = np.arange( -ltime_len/2, ltime_len/2, ltime_interval )

#——————————————————————————————————————————————————————————————————
# 绘制H1 Strain，使用来自“H1”探测器的数据作图：

fig = plt.figure( figsize = ( 12, 6 ) )   #创建一个大小位12*6的绘图空间
#---------------------------------------------------
# 画出以时间位X轴，应变数据为Y轴的图像，并设置标题和坐标轴的标签。
plth = fig.add_subplot( 221 )
plth.plot( htime,hstrain, 'y' )
plth.set_xlabel( 'Time(seconds)' )
plth.set_ylabel( 'H1 Strain' )
plth.set_title( 'H1 Strain' )
#-------------------------------------------------------

#—————————————————————————————————————————————————————————————————
#绘制L1 Strain & Template.

#以完全相同的方法绘制另外两幅图像。 
#分别放在绘图区域的第一列右边和第二列

pltl = fig.add_subplot(222)
pltl.plot( ltime, lstrain, 'g' )
pltl.set_xlabel( 'Time(seconds)' )
pltl.set_ylabel( 'L1 Strain' )
pltl.set_title( 'L1 Strain' )

pltref = fig.add_subplot( 212 )
pltref.plot( reftime, ref_H1 )
pltref.set_xlabel( 'Time(sceonds)' )
pltref.set_ylabel( 'Template Strain' )
pltref.set_title( 'Template' )
fig.tight_layout( )

#—————————————————————————————————————————————————————————————————
#显示并保存图像：
fig.tight_layout( )  #自动调整图像外部边缘。

plt.savefig( "引力波的绘制-副本.png" )
plt.show( )
plt.close( fig )


