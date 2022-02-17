
# -—————————————————— 体育竞技分析_0.3 ——————————————————————　#

# ----- 好吧，没啥大变化，为了解并掌握代码而编写 -----#
# ----- 内容化繁为简也是一种自顶向下模式 ----- #

from random import random

def printIntro( ):
    print ("两个：选手 A 和 B 的竞技比赛。")
    print ( "需要 A 和 B 的能力值 （0——1之间的小数表示或者是大于1的数值）。" )

def getInputs( ):
    a = eval (input ( " A 的能力值（0--1）：" ) )
    b = eval (input ( " B 的能力值（0--1）：" ) )
    n = eval (input ( "比赛场次：" ) )
    return a , b , n


def simNGames ( n , probA , probB ):
    winsA , winsB = 0 , 0
    for i in range ( n ):
        scoreA , scoreB = simOneGame ( probA , probB )
        if scoreA > scoreB :
           winsA += 1
        else:
            winsB += 1
    return winsA , winsB

def gameOver( a , b ):
    return a == 15 or b ==15

def simOneGame ( probA , probB ):
    scoreA , scoreB = 0 , 0
    serving = "A"
    while not gameOver ( scoreA , scoreB ):
        if serving == "A":      # serving =serve( 发球 )
            if random() < probB:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA , scoreB

def printSummary( winsA , winsB ):
    n = winsA + winsB
    print ( "竞技分析开始，共进行{}场比赛" .format(n) )
    print ( "选手A或胜{}场比赛，占比{:0.1%}" .format( winsA , winsA /n ) )
    print ( "选手B或胜{}场比赛，占比{:0.1%}".format( winsB, winsB / n ) )

def main():
    printIntro()
    probA , probB , n = getInputs()
    winsA , winsB = simNGames ( n , probA , probB )
    printSummary ( winsA , winsB )

main()
