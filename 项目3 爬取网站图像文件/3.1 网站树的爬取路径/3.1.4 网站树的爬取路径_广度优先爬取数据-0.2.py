# 广度优先爬取数据
# 客户端程序
# -0.2-


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

start_url = "http://127.0.0.1:5000"
Q=Queue
Q.enter(start_url + "books.html")
while not Q.empty():
    url = Q.fetch()
    resp = urllib.request.urlopen(url)
    data = resp.read()
    data = data.decode()
    soup = BeautifulSoup(data, "lxml")
    print(soup.select("h3")[0].text)
    links = soup.select("a")
    for link in links:
        url = start_url + link["href"]
        Q.enter(url)


