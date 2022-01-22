#**************************************************
# 5.6.3 Selenium 强制等待
#**************************************************


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options )

driver.get("http://127.0.0.1:5000")

# 设置强制等待 1.5 秒.
# 在经过等待 1.5 秒后程序从服务器获取了元素，爬取了数据.
# 如果设置的强制等待时间不够长（例如：0.5秒），还是爬取不到需要的数据。
time.sleep(1.5)

marks = driver.find_elements_by_xpath("//select/option")
print("品牌数量：", len(marks))

for mark in marks:
    print(mark.text)
form = driver.find_element_by_xpath("//form")
print(form.get_attribute("innerHTML").strip())

time.sleep(3)

driver.close()

