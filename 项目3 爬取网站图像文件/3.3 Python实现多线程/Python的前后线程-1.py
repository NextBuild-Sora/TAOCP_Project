
# ---- python的前后台线程 ---- #


#例3-3-1： 在主线程中启动一个子线程执行reading函数。
import threading
import time
import random

def reading():
    for i in range(10):
        print("子线程：", i)
        time.sleep(random.randint(1, 2))

r = threading.Thread(target = reading)
r.setDaemon(False)  #后台线程
r.start()
print("主线程，结束！")


