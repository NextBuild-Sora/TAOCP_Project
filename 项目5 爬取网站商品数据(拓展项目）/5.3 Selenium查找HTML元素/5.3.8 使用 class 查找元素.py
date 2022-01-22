#***********************************
#
# 5.3.8 使用 class 查找元素
#
#***********************************


from selenium import webdriver

# 指定chrome.exe绝对路径。设置binary_location属性:
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver=webdriver.Chrome(options= options)
driver.get('http://127.0.0.1:5000')

#例 5-3-19: 查找网页 class="pl"的所有元素
e = driver.find_element_by_class_name("pl")     #查找第一个 class=value 的元素.
print(e.text)
f = driver.find_element_by_class_name("title")
print(f.text)
f = driver.find_element_by_class_name("date")
print(f.text)

print("#********************************************#")
elems = driver.find_elements_by_class_name("pl")    #查找所有 class=value 元素.
for elem in elems:
    print(elem.text)

print("#***********************************************#")
#也可以通过下列方式查找:
elems = driver.find_element_by_xpath("//span[@class='pl']")
print(elems.text)
elems = driver.find_element_by_css_selector("span[class='pl']")
print(elems.text)

#关闭
driver.close()


