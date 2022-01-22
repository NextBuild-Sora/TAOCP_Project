#**************************************
# 爬取Chindaliy网站的旅游数据与图像
#**************************************


import urllib.request
from bs4 import BeautifulSoup

url = "http://www.chinadaily.com.cn/travel/citytours"

def getHtml(url):
    resp = urllib.request.urlopen(url)
    data = resp.read()
    html = data.decode()
    return html

html = getHtml(url)
print(html)


