#**************************************
# 爬取Chindaliy网站的旅游数据与图像
# -0.3-
#**************************************


import urllib.request
from bs4 import BeautifulSoup

url = "http://www.chinadaily.com.cn/travel/citytours"

def getHtml(url):
    resp = urllib.request.urlopen(url)
    data = resp.read()
    html = data.decode()
    return html

def spider(url):
    global count

    html = getHtml(url)
    soup = BeautifulSoup(html, "lxml")
    div = soup.select_one('div[class="lft_art lf"][id="left"]')
    divs = div.select('div[class="mb10 tw3_01_2"]')
    for div in divs:
        title = div.select_one("span h4").text
        count = count + 1
        print("标题：")
        print("%-5d %s" %(count , title))
        print()

 
count = 0
spider(url)



