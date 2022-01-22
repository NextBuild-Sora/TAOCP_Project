
# 3.2 网站图的爬取路径_
# 改进广度优先---客户端程序
# 版本-2-


from bs4 import BeautifulSoup
import urllib.request

class Queue:    #队列
    def __init__ (self):
        self.st = []
    def fetch(self):
        return self.st.pop(0)
    def enter(self, obj):
        self.st.append(obj)
    def empty(self):
        return len(self.st) == 0

def visit(url):     #要访问的站点
    global  urls
    if url in urls:
        return []
    urls.append(url)

    try:
        data = urllib.request.urlopen(url)
        data = data.read()
        data = data.decode()
        soup = BeautifulSoup(data, "lxml")
        print(soup.find("h3").text)
        links = soup.select("a")
        return links
    except Exception as e:
        print("错误：", e)

start_url = "http://127.0.0.1:5000/"
urls = []

Q = Queue()
Q.enter(start_url)
while not Q.empty():
    url = Q.fetch()
    links = visit(url)
    for link in links:
        url = start_url + link["href"]
        Q.enter(url)

print("结束！")


