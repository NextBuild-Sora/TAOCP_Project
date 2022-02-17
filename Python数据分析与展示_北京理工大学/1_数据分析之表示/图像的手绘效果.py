
# --- 图像的手绘效果 --- #

#***********************************************#
#            手绘效果的几个特征： 
#            • 黑白灰色 .
#            • 边界线条较重 .
#            • 相同或相近色彩趋于白色 .
#            • 略有光源效果 .
#***********************************************#


from PIL import Image
import numpy as np 

a = np.asarray( Image.open( 'D:/文档/Python文件/图像手绘效果/bejing.jpg' ).convert('L') ).astype('float')

depth = 10.                 # （0-100）预设深度值。
grad = np.gradient(a)       # 取图像灰度的梯度值。
grad_x, grad_y = grad       # 分别取横纵图像梯度值。提取x和y方向的梯度值。

#根据深度调整x和y方向的梯度值。
grad_x = grad_x*depth/100.  
grad_y = grad_y*depth/100.

A = np.sqrt( grad_x**2 + grad_y**2 + 1. )       #构造x和y轴梯度的三维归一化单位坐标系。
uni_x = grad_x/A
uni_y = grad_y/A              
uni_z = 1./A

vec_el = np.pi/2.2      # 光源的俯视角度，弧度值。
vec_az = np.pi/4        # 光源的方位角度，弧度值。

# np.cos(vec_el)为单位光线在地平面上的投影长度；dx, dy, dz是光源对x/y/z三方向的影响程度。
dx = np.cos(vec_el)*np.cos( vec_az )     #光源对x轴的影响。
dy = np.cos(vec_el)*np.sin( vec_az )     #光源对y轴的影响。
dz = np.sin(vec_el)                      #光源对z轴的影响。

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)    #光源归一化。#梯度与光源相互作用，将梯度转化为灰度。
b = b.clip(0,255)     #为避免数据越界，将生成的灰度值裁剪至0‐255区间。

#生成图像。
im = Image.fromarray(b.astype('uint8'))     #重构图像。
im.save('D:/文档/Python文件/图像手绘效果/北京_手绘-1.png')

print (" 保存。。 ")



