
# 3.2 网站图的爬取路径_改进深度优先客户端程序
# 版本-2-


from bs4 import BeautifulSoup
import urllib.request

class Stack:
    def __init__(self):
        self.st = []
    def pop(self):
        return self.st.pop()
    def push(self, obj):
        self.st.append(obj)
    def empty(self):
        return len(self.st) == 0


def visit(url):
    global urls
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
        return  links
    except Exception as e:
        print("错误：", e)

def spider(url):
    links = visit(url)
    for link in links:
        url = start_url + link["href"]
        spider(url)

def DFS():
    st=Stack()
    st.push(start_url + "books.html")
    while not st.empty():
        url = st.pop()
        links = visit(url)
        #for link in links:
            # url = start_url + link["href"]
        for i in range(len(links)-1, -1, -1):     #从左到右的顺序
            url=start_url+links[i]["href"]    #从左到右的顺序

            st.push(url)

start_url = "http://127.0.0.1:5000/"
urls = []
spider(start_url + "books.html")
print()
urls = []
DFS = []

print("结束！")

