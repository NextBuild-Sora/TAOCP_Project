

# ---* 图像处理库（PIL）操作 *--- #
# 实例1：模糊效果。



from PIL import Image, ImageFilter

im = Image.open( 'D:/文档/Python文件/Python语言基础与应用_北京大学/08-getty.jpg' )

im2 = im.filter( ImageFilter.BLUR )
im2.save( 'D:/文档/Python文件/Python语言基础与应用_北京大学/08-getty-模糊.png', 'jpeg' )



