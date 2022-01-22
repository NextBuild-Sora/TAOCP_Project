
#************************************************#
# 5.4.2 Selenium 使用元素动作
# 1.键盘输入动作
#************************************************#


from selenium import webdriver
import time


try:
#driver = webdriver.Chrome()


# 指定chrome.exe绝对路径。设置binary_location属性:
    options=webdriver.ChromeOptions()
    options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
    driver=webdriver.Chrome(options= options)

    driver.get("http://127.0.0.1:5000")
    user = driver.find_element_by_name("user")
    pwd = driver.find_element_by_name("pwd")
    time.sleep(1)   #睡眠1秒。
    user.send_keys("xxx")   #模拟键盘在元素中输入字符串。
    time.sleep(1)
    pwd.send_keys("123")    #模拟键盘在元素中输入字符串。
except Exception as err:
    print("错误：", err)

#input("Strike any key to finish...")    #任意键结束。。
input("按任意键结束。。。")    #任意键结束。。

#driver.close()



