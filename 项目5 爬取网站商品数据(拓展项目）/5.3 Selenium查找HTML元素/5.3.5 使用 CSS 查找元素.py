#*****************************************
#
# --- 5.3.5 使用 CSS 查找元素 ---
#
###########################################

#   (1) 一个元素：函数 find_element_by_css_selector(css)
#   (2) 元素组成的列表：函数 find_elements_by_css_selector(css)
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

#例 5-3-13: 查找网页中手机品牌
print("品牌：", driver.find_element_by_css_selector("div[class='info'] span[name = 'mark']").text)

print()
#例 5-3-14: 查找网页中手机图像地址
#print(driver.find_element_by_css_selector("div[class='mark']>div").get_attribute("src"))   #抛出异常

#例 5-3-14.1: 查找网页中<div class='mark'>下面的所有元素
print("元素列表（for循环）：")
elems = driver.find_elements_by_css_selector("div[class='mark'] *")
for elem in elems:
    print(elem.text)

#例 5-3-15: 查找网页中手机型号
print("型号：", driver.find_element_by_css_selector("#title").text)

print()

#查看每一个span的text内容
try:
    sp = driver.find_elements_by_css_selector("div[class='info'] div[class='mark'] span")
    for s in sp:
        print(s.text)
except:
    pass



driver.close()  #关闭

