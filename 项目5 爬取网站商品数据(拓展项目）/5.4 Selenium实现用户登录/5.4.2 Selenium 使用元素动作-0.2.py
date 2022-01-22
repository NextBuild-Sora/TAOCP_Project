
#************************************************#
# 5.4.2 Selenium 使用元素动作-0.2
# 1.键盘输入动作
# 2.鼠标点击动作
#************************************************#


from selenium import webdriver
import time


try:

# 指定chrome.exe绝对路径。设置binary_location属性:
    options=webdriver.ChromeOptions()
    options.binary_location=r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
    driver=webdriver.Chrome(options= options)

    driver.get("http://127.0.0.1:5000")
    user = driver.find_element_by_name("user")
    pwd = driver.find_element_by_name("pwd")
    time.sleep(1)   #睡眠1秒。
    user.send_keys("xxx")   #1.0 键盘：模拟键盘在元素中输入字符串。
    time.sleep(1)
    pwd.send_keys("123")    #1.1 键盘：模拟键盘在元素中输入字符串。

    #2.0 鼠标：使用 click()函数实现鼠标点击；提交按钮点击后就提交表单.
    bt = driver.find_element_by_name("login")
    bt.click()  #注：程序自动点击。

except Exception as err:
    print("错误：", err)

#input("Strike any key to finish...")    #任意键结束。。
input("按任意键结束。。。")    #任意键结束。。

#driver.close()



