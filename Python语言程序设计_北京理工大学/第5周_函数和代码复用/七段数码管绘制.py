# ----------------------------------------------- #

# --------------- 七段数码管绘制 ----------------- #
'''

        基本思路
            - 步骤1：绘制单个数字对应的数码管 
            - 步骤2：获得一串数字，绘制对应的数码管 
            - 步骤3：获得当前系统时间，绘制对应的数码管

'''
# ----------------------------------------------- #


import turtle as t
def dL(draw):       # dL=drawLine  绘制单段数码管。
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
def dDt(digit):     # dDt=drawDigit  根据数字绘制七段数码管。
    dL(True) if digit in [2,3,4,5,6,8,9] else dL(False)
    dL(True) if digit in [0,1,3,4,5,6,7,8,9] else dL(False)
    dL(True) if digit in [0,2,3,5,6,8,9] else dL(False)
    dL(True) if digit in [0,2,6,8] else dL(False)
    t.left(90)
    dL(True) if digit in [0,4,5,6,8,9] else dL(False)
    dL(True) if digit in [0,2,3,5,6,7,8,9] else dL(False)
    dL(True) if digit in [0,1,2,3,4,7,8,9] else dL(False)
    t.left(180)
    t.penup()   # 为绘制后续数字确认位置。
    t.fd(20)    # 为绘制后续数字确认位置。
def dDe(date):      # dDe=drawDate  获得要输出的数字。
    for i in date:
        dDt(eval(i))    # 通过eval()函数将数字变为整数
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    dDe('20201011')
    t.hideturtle()
    t.done()
main ()




