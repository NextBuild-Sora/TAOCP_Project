################################################
#
# Selenium 爬虫程序
# -2-
################################################
#   Selenium 模拟浏览器访问网站的方法来获取网页文档，
#   然后从中爬取要的数据，
#   这样的爬虫程序功能就比较强大了。
#
################################################


#(1) 程序先从 selenium 引入 webdriver，引入 chrome 程序的选择项目 Options:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#chrome_options = Options()

#(2) 设置启动 chrome 时不可见：
Options.add_argument('--headless')
Options.add_argument('--disable-gpu')

#(3)创建 chome 浏览器:
driver = webdriver.Chrome(chrome_options=Options)

driver.get("http://127.0.0.1:5000")     #(4) 使用 driver.get(url)方法访问网页

html = driver.page_source       #(5) 通过 driver.page_source 获取网页 HTML 代码
soup = BeautifulSoup(html, "lxml")

hMsg = soup.find("span", attrs = {"id":"hMsg"}).text
print("hMsg内容：", hMsg)
jMsg = soup.find("span", attrs = {"id":"jMsg"}).text
print("内容2：", jMsg)
sMsg = soup.find("span", attrs = {"id":"sMsg"}).text
print("内容3：", sMsg)


