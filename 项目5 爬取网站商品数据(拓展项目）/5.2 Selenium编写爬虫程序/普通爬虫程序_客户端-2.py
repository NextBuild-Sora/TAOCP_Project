##########################################################################
# 普通爬虫程序                                                             #
# 客户端                                                                  #
# 通过 urllib.request 直接访问"http://127.0.0.1:5000"获取 HTML代码           #
# 使用 BeautifulSoup 解析得到数据                                           #
##########################################################################


from bs4 import BeautifulSoup
import urllib.request

resp=urllib.request.urlopen("http://127.0.0.1:5000")
html=resp.read()
html=html.decode()
soup=BeautifulSoup(html, "lxml")

hMsg=soup.find("span", attrs={"id":"hMsg"}).text
print(hMsg)

jMsg=soup.find("span", attrs={"id":"jMsg"}).text
print(jMsg)

sMsg=soup.find("span", attrs={"id":"sMsg"}).text
print(sMsg)


#########################################################################
#                                                                       #
#   显然如果我们通过该方法获取网页 HTML 文档然后进行数据爬取，                    #
# 那么只能爬取 hMsg的信息"HTML Message"，但是爬取不到 jMsg 与 sMsg 的信息的！   #
#                                                                       #
#########################################################################



