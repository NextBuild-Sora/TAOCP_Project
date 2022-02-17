# 科赫雪花的绘制

import turtle as t
def koch(size, n):
    if n == 0:
            t.fd(size)
    else:
        for angle in [0, 60, -120,60]:
            t.left(angle)
            koch(size/3, n-1)
def main():
    t.setup(800,800)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(4)
    level = 3   # 3阶科赫雪花，阶数
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
main()

