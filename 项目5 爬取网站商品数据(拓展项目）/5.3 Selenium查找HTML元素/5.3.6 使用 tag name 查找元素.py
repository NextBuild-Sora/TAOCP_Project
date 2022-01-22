#***********************************
#
# 5.3.6 使用 tag_name 查找元素
#
#***********************************


from selenium import webdriver

# 指定chrome.exe绝对路径。设置binary_location属性:
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver=webdriver.Chrome(options= options)
driver.get('http://127.0.0.1:5000')

#例 5-3-16: 查找<div class='mark'>元素下面的所有<span>元素
elem=driver.find_element_by_xpath("//div[@class='mark']")
elems = elem.find_elements_by_tag_name("span")
for e in elems:
    print(e.text)

#例 5-3-17: 查找网页中手机型号
print(driver.find_element_by_tag_name("h3").text)

#查找一组sapn: 
try:
    sp = driver.find_elements_by_tag_name("span")
    for i in sp:
        print(i.text)
except:
    pass

print()

#一组超链接文本：
try:
    sp = driver.find_elements_by_tag_name("a")
    for s in sp:
        print(s.text)
except:
    pass


#关闭
driver.close()

