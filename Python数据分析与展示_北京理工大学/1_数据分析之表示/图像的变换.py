

# --- 图像的数组表示 --- #

#********************************************************#
#      读入图像后，获得像素RGB值，修改后保存为新的文件.      #
#********************************************************#


from PIL import Image 
import numpy as np 

a = np.array( Image.open( "D:/文档/Python文件/图像手绘效果/fcity.jpg" ) )
print ( "图像的数组：", a.shape, " |  数据类型：", a.dtype )

b = [ 255, 255, 255 ] - a  #

im = Image.fromarray( b.astype('uint8'))
im.save( "D:/文档/Python文件/图像手绘效果/fcity_变换-1.png" )

print ( "保存。" )




