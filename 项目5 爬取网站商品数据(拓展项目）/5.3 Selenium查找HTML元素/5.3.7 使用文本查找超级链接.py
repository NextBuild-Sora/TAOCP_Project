#***********************************
#
# 5.3.7 使用文本查找超级链接
#
#***********************************


from selenium import webdriver

# 指定chrome.exe绝对路径。设置binary_location属性:
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver=webdriver.Chrome(options= options)
driver.get('http://127.0.0.1:5000')

'''
#例 5-3-18: 查找网页<a href="#">移动联通<a>元素
print( driver.find_element_by_xpath("//div[@class='detail']/a").text )
print( driver.find_element_by_link_text("移动联通").text )      #查找（完全匹配）第一个文本值为 text 的超级链接元素<a>。
print( driver.find_element_by_partial_link_text("联通").text )      #查找部分接链文本。
'''


try:
    a = driver.find_element_by_link_text("双开双待")
    print(a.text)

    b = driver.find_element_by_partial_link_text("联通")
    print(b.text)

except:
    print("Pass！！！")

#关闭
driver.close()


