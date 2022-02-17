

# --- 图像的变换 --- #
# -0.2-

#********************************************************#
#      读入图像后，获得像素RGB值，修改后保存为新的文件.      #
#********************************************************#


from PIL import Image 
import numpy as np 

a = np.array( Image.open( "D:/文档/Python文件/图像手绘效果/beijing.jpg" ).convert('L'))

b = 255 - a

im = Image.fromarray( b.astype('uint8') )
im.save( "D:/文档/Python文件/图像手绘效果/bejing_变换-1.png" )

print ("保存。")


#优化-1 ：
a1 = np.array( Image.open( "D:/文档/Python文件/图像手绘效果/beijing.jpg" ).convert('L') )
c = (100/255)*a + 150   #区间变换
im = Image.fromarray(c.astype('uint8'))
im.save( "D:/文档/Python文件/图像手绘效果/北京_变换-1.png" )

print("保存-----2 。")


#优化-2 ：
a2 = np.array(Image.open( "D:/文档/Python文件/图像手绘效果/beijing.jpg" ).convert('L'))
d = 255 * (a/255)**2    #像素平方

im = Image.fromarray( d.astype('uint8') )
im.save( "D:/文档/Python文件/图像手绘效果/北京_变换-2.png" )

print("保存----3 ")


