
#深度优先爬取数据
#客户端程序

'''
    如果我们不使用递归程序实现深度优先的顺序爬取网站数据，
也可以设计一个栈Stack来完成。


'''

from bs4 import BeautifulSoup
import urllib.request

class Stack:
    def __init__(self):
        self.st = []
    def pop(self):  #出栈。
        return self.st.pop()
    def push(self, obj):    #压栈。
        self.st.append(obj)
    def empty(self):     #判断栈是否为空。
        return len(self.st) == 0

def spider(url):
    stack = Stack()
    stack.push(url)
    while not stack.empty():
        url = stack.pop()
        try:
            data=urllib.request.urlopen(url)
            data=data.read()
            data=data.decode()
            soup=BeautifulSoup(data, "lxml")
            print(soup.find("h3").text)
            links=soup.select("a")
            for i in range(len(links)-1, -1, -1):
                href=links[i]['href']
                url=start_url + "/" + href
                stack.push(url)
        except Exception as err:
            print("错误信息：", err)

start_url = "http://127.0.0.1:5000"
spider(start_url)
print("结束！！！")

