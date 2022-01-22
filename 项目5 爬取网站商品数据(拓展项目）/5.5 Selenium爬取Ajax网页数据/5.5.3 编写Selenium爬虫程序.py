#********************************************
# 5.5.3 编写爬虫程序
# 使用 Selenium 模拟浏览器去浏览网页，
# 然后再模拟用户选择<select>中各个手机品牌的过程实现换页，
# 就可以逐页爬取所有的手机数据了.
#********************************************


from selenium import webdriver
import time

# (3) spider 函数负责爬取当前页面的所有手机记录。
def spider(index):
    trs = driver.find_elements_by_tag_name('tr')    #获取所用的<tr>元素
    for i in range(1, len(trs)):
        tds = trs[i].find_elements_by_tag_name("td")
        model = tds[0].text     #手机的型号
        price = tds[1].text     #价格
        print("%-16s%-16s" % (model, price))
    select = driver.find_element_by_id("marks")
    options = select.find_elements_by_tag_name("option")
    if index < len(options)-1:  #index 变量记录是第几个<option>被选择.
        index += 1  #在一个页面被爬取后 index 增加1.
        #调用 options[index].click()选择新页面继续爬取数据，一直到最后一个<option>被选择为止.
        options[index].click()  #模拟用户点击该<option>的动作.
        time.sleep(0.5)
        spider(index)   # spider 被递归调用


#(1) 创建一个浏览器对象 driver，使用这个 driver 对象模拟浏览器。
options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options )

#(2) 访问 http://127.0.0.1:5000 网站，爬取第一个页面的手机数据。
driver.get("http://127.0.0.1:5000")     #浏览网站的第一页
spider(0)

driver.close()


