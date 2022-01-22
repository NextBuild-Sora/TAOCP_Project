#*************************************************
# Selenium 爬虫程序
#   它是一个浏览器，在浏览一个网页后会在它内部构建一棵
# HTML元素结构树，
# 编写下列程序查看 HTML 代码：
#************************************************


from selenium import webdriver
'''
# 使用此方法，出现浏览器二进制文件错误。

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
'''

#设置浏览器二进制文件的位置：
options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options)

driver.get("http://127.0.0.1:5000")

print(driver.page_source)

driver.close()


