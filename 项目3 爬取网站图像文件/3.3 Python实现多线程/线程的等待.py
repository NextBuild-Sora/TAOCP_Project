
# --- 线程的等待 --- #

import threading
import time
import random


print()
print("例3-3-4：")
#例3-3-4：主线程启动一个子线程并等待子线程结束后才继续执行。

def reading():
    for i in range(5):
        print("reading", i)
        time.sleep(random.randint(1, 2))

t=threading.Thread(target = reading)
t.setDaemon(False)
t.start()
t.join()    #当前的线程就会停止执行；这条语句启动阻塞等待的作用
print("The End")


print()
print("例3-3-5：")
#例3-3-5：在一个子线程启动另外一个子线程，并等待子线程结束后才继续执行。

def reading():
    for i in range(5):
        print("reading", i)
        time.sleep(random.randint(1, 2))

def test():
    r=threading.Thread(target=reading)
    r.setDaemon(True)
    r.start()
    r.join()    #阻塞
    print("test end")

t=threading.Thread(target=test)
t.setDaemon(False)
t.start()
t.join()    #阻塞
print("The End")


