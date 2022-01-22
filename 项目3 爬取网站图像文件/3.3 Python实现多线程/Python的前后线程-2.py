
# ---- python的前后台线程 ---- #


#例3-3-2： 启动一个前台线程
import threading
import time
import random

def reading():
    for i in range(5):
        print("子线程：", i)
        time.sleep(random.randint(1, 2))

r = threading.Thread(target = reading)
r.setDaemon(True)  #前台线程
r.start()
print("主线程，结束！")


