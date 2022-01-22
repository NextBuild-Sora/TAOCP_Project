#**************************************
# 爬取Chindaliy网站的旅游数据与图像
# -0.2-
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
#print(html)

soup = BeautifulSoup(html, "lxml")
div = soup.select_one('div[class="lft_art lf"][id="left"]')
#print(div)

divs = div.select('div[class="mb10 tw3_01_2"]')
#print(len(divs))

for div in divs:
    title = div.select_one("span h4").text
    print("标题：", title)

 
