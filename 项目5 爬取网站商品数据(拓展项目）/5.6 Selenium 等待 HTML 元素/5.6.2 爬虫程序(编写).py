#***********************************************
#
# 5.6.2 编写爬虫程序
# 编写一个爬虫程序去爬取手机的所有品牌与所有颜色，
# 并选择其中的一个品牌与颜色进行提交。
#
#************************************************


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options )
#driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000")

marks = driver.find_elements_by_xpath("//select/option")
print("品牌数量：", len(marks))

for mark in marks:
    print(mark.text)

form = driver.find_element_by_xpath("//form")
print( form.get_attribute("innerHTML").strip() )

time.sleep(2)

driver.close()


