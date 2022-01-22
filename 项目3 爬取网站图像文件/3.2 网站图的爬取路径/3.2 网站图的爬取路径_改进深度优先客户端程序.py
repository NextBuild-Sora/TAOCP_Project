#改进深度优先遍历
#图的深度优先遍历
#客户端

"""
    图的深度优先遍历类似于树的前序遍历。采用的搜索方法的特点是
尽可能先对纵深方向进行搜索。这种搜索方法称为深度优先搜索
(Depth-First Search)。
相应地，用此方法遍历图就很自然地称之为
图的深度优先遍历，基本实现思想：
（1）访问顶点v；
（2）从v的未被访问的邻接点中选取一个顶点w，从w出发进行深度优先遍历；
（3）重复上述两步，直至图中所有和v有路径相通的顶点都被访问到。

"""

from bs4 import BeautifulSoup
import urllib.request

#1、使用递归:

def spider(url):
    global urls
    if url not in urls:
        urls.append(url)
        try:
            data=urllib.request.urlopen(url)
            data=data.read()
            data=data.decode()
            soup=BeautifulSoup(data, "lxml")
            print(soup.find("h3").text)
            links=soup.select("a")
            for link in links:
                href=link["href"]
                url=start_url + "/" + href
                spider(url)
        except Exception as err:
            print("错误：", err)

print("递归：")
start_url="http://127.0.0.1:5000"
urls=[]
spider(start_url)
print("结束！！！")

print()

#2、使用栈：
class Stack:
    def __init__(self):
        self.st=[]
    def pop(self):
        return self.st.pop()
    def push(self, obj):
        self.st.append(obj)
    def empty(self):
        return len(self.st)==0

def spider(url):
    global urls
    stack=Stack()
    stack.push(url)
    while not stack.empty():
        url=stack.pop()
        if url not in urls:
            urls.append(url)
            try:
                data=urllib.request.urlopen(url)
                data=data.read()
                data=data.decode()
                soup=BeautifulSoup(data, "lxml")
                print(soup.find("h3").text)
                links=soup.select("a")
                for l in range(len(links)-1, -1, -1):
                    href=links[i]["href"]
                    url=start_url + "/" + href
                    stack.push(url)
            except Exception as err:
                print("错误：", err)

print("栈：")
start_url="http://127.0.0.1:5000"
urls=[]
spider(start_url)
print("结束！！！")

