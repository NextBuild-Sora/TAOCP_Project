
# ---- python的前后台线程 ---- #


#例3-3-3： 前台与后台线程
import threading
import time
import random

def reading():
    for i in range(5):
        print("读数（子线程）：", i)
        time.sleep(random.randint(1, 2))

def test():
    r = threading.Thread(target=reading)
    r.setDaemon(True)   #前台子线程
    r.start()
    print("前台 test end")

t = threading.Thread(target=test)
t.setDaemon(False)  #后台
t.start()
print("主线程 The End")




