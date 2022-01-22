#####################################################
#
# --- 5.3 Selenium查找HTML元素 ---
#
###################################################

#***********************************************************
# 5.3.2 使用 XPath 查找元素   ********************************
#
# 使用 XPath 查找主要有两个函数：   ****************************
#   (1) 函数 find_element_by_xpath(xpath)：
#       查找 xpath 匹配的第一个元素，
#       如果找到就返回一个 WebElement 类型的对象，如果找不到就抛出异常；
#   (2) 函数 find_elements_by_xpath(xpath)：
#       查找 xpath 匹配的所有元素组成的列表，
#       每个元素都是一个 WebElement 对象，如果找不到就返回空列表；
#   (3) 任 何 一 个 WebElement 对 象 都 可 以 调 用
#       find_element_by_xpath 与 find_elements_by_xpath 函数。
####################################################


from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#driver = webdriver.Chrome(chrome_options = chrome_options)

# 指定chrome.exe绝对路径。设置binary_location属性:
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver=webdriver.Chrome(options= options)

driver.get("http://127.0.0.1:5000")

#例 5-3-1: 查找网页元素<h3>
elem = driver.find_element_by_xpath("//div[@class='info']//h3")
print(type(elem))
print(elem)

print()

# 例 5-3-2: 查找网页中元素<h4>
try:
    e=driver.find_element_by_xpath("//div[@class='info']//h4")      #注：无此h4。
    #print(type(elem))
    print(e)
except Exception as err:
    print("错误：", err)

#driver.close()


