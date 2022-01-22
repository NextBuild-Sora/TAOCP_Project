
"""
--递归程序--
    爬取这个网站各个网页的<h3>的标题值，设计的思想如下：
(1) 从books.htm出发；
(2) 访问一个网页，获取<h3>标题；
(3) 获取这个网页中所有<a>超级链接的href值形成links列表；
(4) 循环links列表，对于每个链接link都指向另外一个网页，递归回到
(2)；
(5) 继续links的下一个link，直到遍历所有link为止；

实际上这种递归程序都是采用深度优先的方法遍历树。

"""


from bs4 import BeautifulSoup
import urllib.request

start_url = "http://127.0.0.1:5000"

def spider(url):
    try:
        data= urllib.request.urlopen(url)
        data = data.read()
        data = data.decode()
        soup = BeautifulSoup(data, "lxml")
        #print(soup.find("h3").text)
        print(soup.select("h3")[0].text)
        links = soup.select("a")
        for link in links:
            href = link["href"]
            url = start_url + "/" + href
            #print(url)
            spider(url)
    except Exception as err:
        print("错误信息：", err)

spider(start_url)
print("深度优先遍历树结束")

