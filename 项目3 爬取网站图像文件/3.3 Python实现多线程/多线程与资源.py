

# --*- 多线程与资源 -*-- #


#例3-3-6：一个子线程A把一个全局的列表words进行升序的排列，另外一个D线程把这个列表进行降序的排列
import threading
import time

lock = threading.RLock()   #来创建一个线程锁对象
#lock = threading._RLock()  #这个可以
words = ["a","b","d","b","p","m","e","f","b"]

def increase():
    global words
    for count in range(5):
        lock.acquire()  #获取线程锁
        print("A acquires")
        for i in range(len(words)): #升序
            for j in range(i+1, len(words)):
                if words[j] < words[i]:
                    t = words[i]
                    words[i] = words[j]
                    words[j] = t
        print("A", words)
        time.sleep(1)
        lock.release()  #释放锁

def decrease():
    global words
    for count in range(5):
        lock.acquire()  #获取线程锁
        print("D acquired")
        for i in range(len(words)): #降序
            for j in range(i+1, len(words)):
                if words[j] > words[i]:
                    t = words[i]
                    words[i] = words[j]
                    words[j] = t
        print("D", words)
        time.sleep(1)   #睡眠
        lock.release()  #释放锁

A = threading.Thread(target = increase)
A.setDaemon(False)
A.start()   #开始

D = threading.Thread(target = decrease)
D.setDaemon(False)
D.start()   #开始
print("The End")


