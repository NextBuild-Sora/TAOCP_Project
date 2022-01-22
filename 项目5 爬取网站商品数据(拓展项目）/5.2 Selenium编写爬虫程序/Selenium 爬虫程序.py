####################################
# Selenium 爬虫程序
####################################


#(1) 程序先从 selenium 引入 webdriver，引入 chrome 程序的选择项目 Options:
from selenium import webdriver
from selenium.webdriver.driver.options import Options

chrome_options = Options()
#(2) 设置启动 chrome 时不可见：
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#(3)创建 chome 浏览器:
chrome = webdriver.Chrome(chrome_options = chrome_options)
driver.get("http://127.0.0.1:5000")     #(4) 使用 driver.get(url)方法访问网页
html = driver.page_source       #(5) 通过 driver.page_source 获取网页 HTML 代码
print(html)
driver.close()      #(6) 使用 driver.close()关闭浏览器


