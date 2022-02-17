

# --- 图像的数组表示 --- #

'''
        图像是一个由像素组成的二维矩阵，每个元素是一个RGB值.
        图像是一个三维数组，维度分别是高度、宽度和像素RGB值.


'''

from PIL import Image 
import numpy as np 

im = np.array( Image.open("D:/文档/Python文件/图像手绘效果/beijing.jpg") )
print ( "图像的数组表示：", im.shape, im.dtype )

