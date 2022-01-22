# 广度优先爬取数据
# 客户端程序

"""
    遍历网站树还有一种广度优先的顺序，这要使用到队列.
    Python中实现一个队列十分简单，Python中的列表list就是一个队列.

"""

# 设计广度优先的顺序爬取数据的客户端程序
from bs4 import BeautifulSoup
import urllib.request


class Queue:  # 设计一个队列类
    def __init__(self):
        self.st = []

    def fetch(self):  # 出列函数
        return self.st.pop(0)

    def enter(self, obj):  # 入列函数
        self.st.append(obj)

    def empty(self):  # 判断列是否为空
        return len(self.st) == 0

def spider(url):
    queue = Queue()
    queue.enter(url)
    while not queue.empty():
        url = queue.fetch()
        try:
            data = urllib.request.urlopen(url)
            data = data.read()
            data = data.decode()
            soup = BeautifulSoup(data, "lxml")
            print(soup.find("h3").text)
            links = soup.select("a")
            for link in links:
                href = link['href']
                url = start_url + "/" + href
                queue.enter(url)
        except Exception as err:
            print("错误信息：", err)


start_url = "http://127.0.0.1:5000"
spider(start_url)
print("结束！！！！")
