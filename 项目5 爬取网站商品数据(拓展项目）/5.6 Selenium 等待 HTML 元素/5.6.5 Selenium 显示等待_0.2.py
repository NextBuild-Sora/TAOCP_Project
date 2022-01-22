#**************************************************
# 5.6.5 Selenium 显示等待.
# -0.2-版
# 2、显示等待.
# Selenium 的显示等待与循环等待有点类似，
# 它是专门等待指定的元素的。
#**************************************************


from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options )

try:
    driver.get("http://127.0.0.1:5000")
    locator = (By.XPATH, "//select/option")
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(locator))
    marks = driver.find_elements_by_xpath("//select/option")
    print("品牌数量：", len(marks))
    for mark in marks:
        print(mark.text)
    form = driver.find_element_by_xpath("//form")
    print("获得的属性：", form.get_attribute("innerHTML").strip())
except Exception as err:
    print("错误：", err)

time.sleep(3)

driver.close()


