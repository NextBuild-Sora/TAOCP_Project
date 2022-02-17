
'''
0、海龟方向控制

1、seth函数 ( 1 )：改变行进方向，海龟走角度。行进方向的绝对角度。

    1 参数：行进方向的绝对角
    
2、left（ a ）：左转，海龟向左转。
    right( a )：右转。

    a：在海龟当前行进方向上旋转的角度

'''
import turtle
turtle.fd (100)
turtle.penup()
turtle.pendown() 
turtle.pensize (10)
turtle.pencolor ('purple')

turtle.seth (45)
turtle.fd (100)
turtle.left (100)
turtle.fd (100)
turtle.seth (-135)
turtle.fd (100)
turtle.right (90)
turtle.fd (100)

turtle.done ()
