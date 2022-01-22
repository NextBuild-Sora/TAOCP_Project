#*****************************************
#
# --- 5.3.3 查找元素的文本与属性 ---
#
# 通过 WebElement 对象可以查找到它的文本与属性。
#   (1) 任何一个 WebElement 对象都可以通过 text 属性获取它的文本，
#   元素的文本值是它与它的所有子孙节点的文字的组合，
# 如果没有就返回空字符串。
#
#   (2) 任何一个 WebElement 对象都可以 通过
# get_attribute(attrName)获取名称为
# attrName 的属性值，
# 如果元素没有 attrName 属性就返回 None。
#
#*****************************************


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('http://127.0.0.1:5000')

#例 5-3-3: 查找网页中第一个<span>元素的文本
print(driver.find_element_by_xpath("//div[@class='info']//span").text)

#例 5-3-5: 查找网页中手机的品牌
print(driver.find_element_by_xpath("//div[@class='info']//span[@name='mark']").text)

#例 5-3-6: 查找网页中手机图像<img>的地址
print(driver.find_element_by_xpath("//div[@class='pic']//ing").get_attribute("src"))

driver.close()



