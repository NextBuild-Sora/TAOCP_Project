

# --- pypiot的中文显示 --- #


import matplotlib.pyplot as plt
import matplotlib
import numpy as np

#-----------------------------------------------#
# 第一种方法：

# 默认并不支持中文显示，需要rcParams修改字体实现.
#-----------------------------------------------#

matplotlib.rcParams[ 'font.family' ]= 'SimHei'
plt.plot([3,1,4,5,2])
plt.ylabel( "纵轴（值）" )
plt.savefig( 'D:/文档/Python文件/Python数据分析与展示/数据分析之展示/test-中文显示-1', dpi = 700 )
plt.show( )


#******************************************************************#
# -- rcParams 属性：
#   --  'font.family' ：用于显示字体的名字。
#   --   'font.style' ：字体风格，正常'normal'或斜体'italic'。
#   --   'font.size'：字体大小，整数字号或者'large'、'x‐small'。
#******************************************************************#

matplotlib.rcParams[ 'font.family' ] = 'SimHei'
matplotlib.rcParams[ 'font.size' ] = 12

a = np.arange( 0.0, 5.0, 0.02 )

plt.xlabel( '横轴：时间' )
plt.ylabel( '纵轴：振幅' )
plt.plot( a, np.cos( 2*np.pi*a ), 'r--' )   #正弦波
plt.savefig( 'D:/文档/Python文件/Python数据分析与展示/数据分析之展示/test-中文显示-2', dpi = 700 )

plt.show( )


#-----------------------------------------------#
# 第二种方法：
# 在有中文输出的地方，增加一个属性：fontproperties . 
#-----------------------------------------------#

plt.xlabel( '横轴：时间', fontproperties = 'simhei', fontsize = 12 )
plt.ylabel( '纵轴：振幅', fontproperties = 'simhei', fontsize = 12 )

#**********************************************************************************#
'''
plt.rcParams['font.sans-serif'] = ['simhei']    #用来正常显示中文标签（字体格式）
plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')

# 可以选择这种方式。
'''
#**********************************************************************************#

plt.plot( a, np.cos( 2*np.pi*a ), 'r--' )
plt.savefig( "D:/文档/Python文件/Python数据分析与展示/数据分析之展示/test-中文显示-3", dpi = 800  )
plt.show( )


