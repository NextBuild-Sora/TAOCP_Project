
# 3.2 网站图的爬取路径_
# 改进广度优先客户端程序


from bs4 import BeautifulSoup
import urllib.request

class Queue:
    def __init__ (self):
        self.st = []
    def fetch(self):
        return self.st.pop(0)
    def enter(self, obj):
        self.st.append(obj)
    def empty(self):
        return len(self.st) == 0

def spider(self):
    global urls
    queue = Queue()
    queue.enter(url)
    while not queue.empty():
        url = queue.fetch()
        if url not in urls:
            try:
                urls.append(url)
                data = urllib.request.urlopen(url)
                data = data.read()
                data = data.decode()
                soup = BeautifulSoup(data, "lxml")
                print(soup.find("h3").text)
                links = soup.select("a")
                for link in links:
                    href = link["href"]
                    url = start_url + "/" + href
                    queue.enter(url)
            except Exception as err:
                print("错误：", err)
start_url = "http://127.0.0.1:5000"
urls = []
spider(start_url)
print("结束！！")

