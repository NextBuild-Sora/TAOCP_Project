
# 文本进度条-V3-版本

import time
sc = 50
print (" 执行开始 " .center( sc // 2 , "-") )
st = time.perf_counter()
for i in range(sc + 1):
    a = '*' * i
    b = '.' * (sc - i)
    c = (i/sc) * 100
    d = time.perf_counter() - st  
    print ( " \r {:^3.0f}% [ {} -> {} ] {:.2f} 秒 " .format( c,a,b,d ), end = ' 100%时为完成！ ' )
    time.sleep(0.1)
print (" \n " + " 执行结束 " .center (sc // 2, "-")) 

