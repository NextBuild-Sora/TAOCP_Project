# 科赫曲线的绘制

import turtle as t
def koch(size, n):
    if n == 0:
            t.fd(size)
    else:
        for angle in [0, 60, -120,60]:
            t.left(angle)
            koch(size/3, n-1)
def main():
    t.setup(800,400)
    t.penup()
    t.goto(-300,-50)
    t.pendown()
    t.pensize(2)
    koch(600,3)
    t.hideturtle()
main()

