

# ---* 图像处理库（PIL）操作 *--- #
# 实例2：添加文字。



from PIL import Image, ImageDraw, ImageFont 

img = Image.open( 'D:/文档/Python文件/Python语言基础与应用_北京大学/08-getty.jpg' )     #打开图片

font = ImageFont.truetype( 'simsun.ttc', 100 )  #设置字体

draw = ImageDraw.Draw( img )    #创建绘图对象

draw.text( (100, 10), "可爱的小猫", (255, 0, 0), font = font )  #添加（设计）文字

img.save( 'D:/文档/Python文件/Python语言基础与应用_北京大学/08-getty-文字.png', 'jpeg' )    #保存图片



