
#****************************************************************************************************#
'''
绘制Pyhon 蟒蛇

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
#*****************************************************************************************************#

from turtle import *   # 程序的关键；引入turtle（海龟） 库
setup ( 650,400,300,300 )    # setup 设置窗体大小及位置（绘图窗体；空间坐标     |    宽度，高度；坐标X轴，坐标Y轴）
penup ()
fd (-250 )
pendown ()
pensize ( 25 )
pencolor ("purple" )
seth ( -40 )    # seth 改变海龟行进方向，只改变方向但不行进

for i in range ( 4 ):     # range 角度
    circle (40,80)   # circle 画圆圈，环绕...移动
    circle (-40,80)
circle(40,80/2)
fd(40)     # fd 前进
circle(16,180)
fd(40 *2/3)
done()

