#**************************************************
# 5.6.5 Selenium 显示等待.
# 1、循环等待.
# 能否爬到数据的关键是<select>中是否已经出现了<option>元素，
# 我们可以设置一个循环来判断是否有<option>元素。
#**************************************************


from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver = webdriver.Chrome(options = options )

try:
    driver.get("http://127.0.0.1:5000")
    waitTime = 0    #使用 waitTime 变量来构造一个循环.
    while waitTime < 10:    #最长等待 10 秒，每间隔 0.5 秒就检查一次<select>中是否有<option>存在.
        marks = driver.find_elements_by_xpath("//select/option")
        if len(marks) > 0:  #如果找到了<option>元素就退出等待循环，不然就继续等待直到<option>出现为止.
            break
        time.sleep(0.5)
        waitTime += 0.5
    if waitTime >= 10:  #如果 10 秒内还没有出现据抛出异常。
        raise Exception("Waiting time out(等待时间)")

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


