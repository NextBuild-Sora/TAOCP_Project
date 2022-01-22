#*****************************************
#
# --- 5.3.4 使用ID和Name查找元素 ---
#
###########################################

#   ID查找：函数 driver.find_element_by_id(id)查找 id 编号的第一个元素，
# 如果查找到就返回一个
# WebElement 对象，如果没有找到就抛出异常。
#
#*****************************************


from selenium import webdriver

'''
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options = chrome_options)
'''

# 指定chrome.exe绝对路径。设置binary_location属性:
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver=webdriver.Chrome(options= options)
driver.get('http://127.0.0.1:5000')

try:
    print(driver.find_element_by_id("title").text)  #例 5-3-9: 查找网页中 id="title"的元素文本。
    print(driver.find_element_by_id("name"))    #例 5-3-10: 查找网页中 id="name"的元素；结果抛出一个异常。
except:
    pass

print()

###############################################
# name 查找元素：
# (1)函数find_element_by_name(value)：查找name = value匹配的第一个元素。
# (2) 函数 find_elements_by_name(value)：查找 name=value匹配的所有元素组成的列表。
###############################################

#例 5-3-11: 查找网页中手机信息
print(driver.find_element_by_name("mark").text)     #品牌
print(driver.find_element_by_name("date").text)     #日期
print(driver.find_element_by_name("price").text)    #价格

print()

#例 5-3-12: 查找网页 name="xxx"的元素；结果抛出一个异常。
try:
    driver.find_element_by_name("xxx")
except Exception as err:
    print(err)



driver.close()  #关闭

