
# ----------------------------------- 体育竞技分析 ----------------------------------- #


from random import random

def printIntro( ):  # 打印介绍（引子）。
    print ( "这个程序模拟两个选手A和B的某种竞技比赛" )
    print ( "程序运行需要A和B的能力值（以0到1之间的小数表示）"  )

def getInputs( ):   # 获得输入。
    a = eval ( input ( "请输入选手A的能力值（0-1）：") )
    b = eval ( input ( "请输入选手B的能力值（0-1）" ) )
    n = eval ( input ( "模拟比赛的场次：" ) )
    return a , b , n

def printSummary ( winsA , winsB ):     # 打印总计：输出获胜结构。
    n = winsA + winsB
    print ( "竞技分析开始，共模拟 {} 场比赛"  .format( n ) )
    print ( "选手A获胜 {} 场比赛，占比 {:0.1%} " .format ( winsA , winsA/n ) )
    print ( "选手B获胜 {} 场比赛，占比 {:0.1%} " .format ( winsB , winsB/n ) )

def genmaOver (a , b):      # 判断一局游戏的结束；当A或B等于15分，比赛结束（返回是是True或False）
    return  a == 15 or b == 15

def simOneGame ( probA , probB ) :      # 模拟一局游戏。
    scoreA , scoreB = 0 , 0     # 成绩（得分）
    serving = "A"
    while not genmaOver ( scoreA , scoreB ): 
        if serving == "A":
            if random( ) < probA:   # 用rnadom函数生成一个随机变量，如果在A运动员能力范围内，A获得一分。
                scoreA += 1     # 在A运动员能力范围内，A获得一分。
            else :
                serving = "B"   # 随机变量超出A能力范围，当前发球局换为B。
        else :
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
    return scoreA , scoreB

def simNGames ( n , probA , probB ):        # 模拟N局（比赛）游戏。
    winsA , winsB = 0 , 0
    for i in range ( n ):
        scoreA , scoreB = simOneGame ( probA , probB )
        if scoreA > scoreB :
            winsA += 1
        else :
            winsB += 1
    return winsA , winsB

def main ( ):       # 主函数
    printIntro ( )      # 介绍（引子）
    probA, probB, n = getInputs ( )     # 获得参数
    winsA, winsB = simNGames ( n, probA, probB )    # 模拟N局的游戏胜利
    printSummary( winsA, winsB )        # 输出获胜次数及概率
    
main( )     # 封装
