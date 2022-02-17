

#********************************************************#

'''

绘制Pyhon 蟒蛇
--------------------------------------------------

import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25) turtle.pencolor("purple") turtle.seth(-40)

for i in range(4):
turtle.circle(40, 80) turtle.circle(-40, 80)

turtle.circle(40, 80/2) turtle.fd(40) turtle.circle(16, 180) turtle.fd(40 * 2/3) turtle.done()
使用IDLE的文件方式 编写代码 并保存为
PythonDraw.py 文件

'''

#********************************************************#


import turtle   # 程序的关键；引入turtle（海龟） 库
turtle.setup ( 650,400,300,300 )    # setup 设置窗体大小及位置（绘图窗体；空间坐标     |    宽度，高度；坐标X轴，坐标Y轴）
turtle.penup ()     # 画笔抬起，海龟在飞行，不绘制任何图像。
turtle.fd (-250 )
turtle.pendown ()   # 画笔落下，海龟爬行，绘制图像。
turtle.pensize ( 25 )   # 画笔宽度，海龟的腰围。
turtle.pencolor ("purple" )     # 画笔颜色，海龟在涂装。
turtle.seth ( -40 )    # seth 改变海龟行进方向，只改变方向但不行进

for i in range ( 4 ):     # range 角度
    turtle.circle (40,80)   # circle  （位置:r半径，角度） 走曲线、画圆圈，默认圆心在海龟左侧r距离的位置。
    turtle.circle (-40,80)
turtle.circle(40,80/2)
turtle.fd(40)     # fd 前进，海龟走直线。
turtle.circle(16,180)
turtle.fd(40 *2/3)
turtle.done()   # done函数：海龟绘制完毕后，窗体不会自动关闭，需要手动关闭；删除这行代码可自动关闭窗体。

