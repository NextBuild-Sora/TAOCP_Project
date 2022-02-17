
# ----------------------- os库的使用 ----------------------- #


# -------------路径操作-------------

import os.path as op

a = op.abspath("../第7周/新时代中国特色社会主义.txt")    # 返回当前系统中的绝对路径（完整路径）
print ('绝对路径：' , a)

b = op.normpath("D://文档//文件")   # 归一化表示形式，统一使用\\分隔路径。
print('归一化:' , b)

c = op.relpath("://文档//Python文件")   #返回当前程序与文件之间的相对路径（relative path）
print ("相对路径：" , c)

#-----------------

a1 = op.dirname("D:\文档\Python文件")   #返回目录名称
print ("返回目录名称：" , a1 )

b1 = op.basename("D:\文档\Python文件")  #最后的文件名称
print ("最后的文件名称：" , b1 )

c1 = op.join("D:/" , "文档/Python文件")     # 组合它们的路径，返回一个路径字符串。
print ("结合路径：", c1)

#-------------------------

a2 = op.exists("D:\文档\Python文件")    #判断文件或目录是否存在。
print("判断文件或目录是否存在：" , a2 )

b2 = op.isfile("D:\文档\Python文件" )   #判断是否为已存在的文件。
print("文件：" , b2)

c3 = op.isdir("D:\文档\Python文件")     #判断是否已存在的目录。
print( "目录：" , c3)

#--------------------------------

a3 = op.getatime("D:\文档\Python文件")  #返回路径文件上次的访问时间。
print("访问时间：" , a3)

b3 = op.getmtime("D:\文档\Python文件")  #返回路径文件最近一次的修改时间。
print("修改时间：" , b3)

cc = op.getctime("D:\文档\Python文件")  #返回路径文件的创建时间。
print( "创建时间：" , cc)

cc0 = op.getsize("D:\文档\Python文件")  #返回文件大小，以字节为单位。
print("文件大小（KB）：" , cc0)



