
# 文本进度条
# 采用字符串方式打印可以动态变化的文本进度条。
# 进度条需要能在一行中逐渐变化

# sleep（）睡觉：模拟一个持续的进度（文本进度条的变化时间）。


import time
scale = 50  # 刻度（数值范围）为：5０。
print ("----- 执行开始 -----")
for i in range ( scale + 1 ):
    a = "*" * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print (' {:^3.0f} % [ {} -> {} ]' .format( c,a,b ) )
    time.sleep(0.1)   # 睡眠时间为：0.1秒。
print ( "----- 执行结束 -----" )

