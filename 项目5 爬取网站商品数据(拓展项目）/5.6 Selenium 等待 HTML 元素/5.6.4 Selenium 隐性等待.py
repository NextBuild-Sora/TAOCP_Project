#**************************************************
# 5.6.4 Selenium 隐性等待
#**************************************************


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options )

#设置隐性加载时间 1.5 秒（网页在加载时最长等待秒数）.
driver.implicitly_wait(1.5)

driver.get("http://127.0.0.1:5000")

marks = driver.find_elements_by_xpath("//select/option")
print("品牌数量：", len(marks))

for mark in marks:
    print(mark.text)
form = driver.find_element_by_xpath("//form")
print("获得的属性：", form.get_attribute("innerHTML").strip())

time.sleep(3)

driver.close()


