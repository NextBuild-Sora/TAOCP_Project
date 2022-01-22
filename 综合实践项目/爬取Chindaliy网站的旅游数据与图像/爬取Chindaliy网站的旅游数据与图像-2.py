#**************************************
# 爬取Chindaliy网站的旅游数据与图像
# -2-
#**************************************


import urllib.request
from bs4 import BeautifulSoup
import time
import os 



url = "http://www.chinadaily.com.cn/travel/citytours"

def getHtml(url):
    try:

        resp = urllib.request.urlopen(url)
        data = resp.read()
        html = data.decode()
        return html
    except Exception as e:
        print("获取网页错误：", e)

def download(ID, src):
    try:
        resp = urllib.request.urlopen(src)
        data = resp.read()  #图像数据
        p = src.rfind(".")
        fileName = ID + src[p:]
        f = open("downloadImages\\" + fileName, "wb")
        f.write(data)
        f.close()
        print("下载：" + fileName)
    except Exception as e:
        print("下载错误：", e)

def spider(url):
    global count, page
    page = page + 1
    print("页面：%3d %s" % (page, url))


    #获取数据
    html = getHtml(url)
    if html == "1":
        return
    soup = BeautifulSoup(html, "html.parser")
    maindiv = soup.select_one('div[class="lft_art lf"][id="left"]')
    divs = maindiv.select('div[class="mb10 tw3_01_2"]')
    for div in divs:
        title = div.select_one("span h4").text
        count = count + 1
        #print("标题：")
        print("%-5d %s" %(count , title))
        #print()

        src = div.select_one("span img")
        if src:
            src = src["src"]
            if src.startswith("//"):
                src="http:"+src
            else:
                src = urllib.request.urljoin(url, src)
            ID = "%04d" %count
            download(ID, src)
    
    #获取下一页的url
    url = ""
    div = maindiv.select_one('div[id="div_currpage"]')
    links = div.select('a[class="pagestyle"]')
    for link in links:
        if link.text == "Next":
            href = link["href"]
            if href.startswith("//"):
                url = "http:"+href
            else:
                url = urllib.request.urljoin(url, href)
            break
    if url:
        #函数的递归调用
        spider(url)


if not os.path.exists("downloadImages"):
    os.mkdir("downloadImages")

count = 0
page = 0

#x = time.clock()    #主要原因是因为python3.8中不支持clock了, 需要替换成time.pref_counter()替换就可以了
#x = time.pref_counter() #报错
x = time.process_time()
spider(url)
y = time.process_time()

print("用时：", (y-x), "秒")



