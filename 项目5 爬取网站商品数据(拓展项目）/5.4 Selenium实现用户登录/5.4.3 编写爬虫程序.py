# ***********************************************
#   --- 5.4.3 编写爬虫程序 ---
# 使用 Selenium 模拟浏览器的浏览过程与用户的登录过程，
# 然后爬取手机的记录。
# ***********************************************

# **************************************************************
"""
    (1)创建一个浏览器对象driver，使用这个driver对象模拟浏览器。

    (2)访问http://127.0.0.1:5000网站，
    获取<input type="text"name="user">
    与<input type="password" name="pwd">元素对象，
    模拟用户键盘输入名称"xxx"与密码“123”。

    (3)获取<input type="submit" name="login">按钮对象，
    执行click()点击动作，提交表单。

    (4)服务器接收提交的user与pwd数据，判断是否登录成功，
    如果登录成功就转"/show"页面显示手机记录。

    (5)爬虫程序爬取数据记录。
"""
# ************************************************************


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def login():
    print(driver.current_url)
    user = driver.find_element_by_name("user")
    pwd = driver.find_element_by_name("pwd")
    login = driver.find_element_by_name("login")
    user.send_keys("xxx")
    pwd.send_keys("123")
    login.click()
    time.sleep(0.5)


def spider():
    print(driver.current_url)
    trs = driver.find_elements_by_tag_name("tr")
    for i in range(1, len(trs)):
        tds = trs[i].find_elements_by_tag_name("td")
        if len(tds) == 3:
            mark = tds[0].text
            model = tds[1].text
            price = tds[2].text
            print("%-16s%-16s%-16s" % (mark, model, price))


# 指定chrome.exe绝对路径。设置binary_location属性:
options=webdriver.ChromeOptions()
options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
driver=webdriver.Chrome(options= options)

'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
'''

try:
    driver.get("http://127.0.0.1:5000")
    login()
    spider()
except Exception as err:
    print("错误信息：", err)

driver.close()

