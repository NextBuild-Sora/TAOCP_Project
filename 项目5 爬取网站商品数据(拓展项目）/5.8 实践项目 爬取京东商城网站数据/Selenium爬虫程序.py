# ************************************
# 5.8 实践项目 爬取京东商城网站数据.
# Selenium爬虫程序.
# ************************************


from selenium import webdriver
import urllib.request
import threading
import sqlite3
import os
import datetime
from selenium.webdriver.common.keys import Keys
import time


# 定义类——我的爬虫
class MySpider:
    #模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64;"
                    " en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"
                }
    imagePath = "download"  #下载地址文件夹

    def startUp(self, url, key):
        # 初始化浏览器.
        options = webdriver.ChromeOptions()
        options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
        self.driver = webdriver.Chrome(options=options)

        # 初始化变量.
        self.threads = []
        self.No = 0
        self.imgNo = 0  #图像编号

        # 初始化数据库
        try:
            self.con = sqlite3.connect("Phones.db")
            self.cursor = self.con.cursor()
            try:
                # 如果有表就删除
                self.cursor.execute("drop table Phones")
            except:
                pass
            try:
                # 建立新的表
                sql = "create tabel Phones (mNo varchar(32) primary key, mMark varchar(256), mPrice varchar(32), mNote varchar(1024), mFile varchar(256))"
                self.cursor.execute(sql)
            except:
                pass
        except Exception as err:
            print("数据库错误：", err)

        # 初始化图像文件夹
        try:
            if not os.path.exists(MySpider.imagePath):
                os.mkdir(MySpider.imagePath)
            images = os.listdir(MySpider.imagePath)
            for img in images:
                s = os.path.join(MySpider.imagePath, img)
                os.remove(s)
        except Exception as err:
            print("图像文件夹错误：", err)

        #网页第一页，输入key后跳转新的页面
        self.driver.get(url)
        keylnput = self.driver.find_element_by_id("key")
        keylnput.send_keys(key)
        keylnput.send_keys(Keys.ENTER)

    # 关闭
    def closeUp(self):
        try:
            self.con.commit()
            self.con.close()
            self.driver.close()
        except Exception as err:
            print("关闭错误：", err)

    # 插入数据记录
    def insertDB(self, mNo, mMark, mPrice, mNote, mFile):
        try:
            sql = "insert into Phones (mNo, mMark, mPrice, mNote, mFile) values (?, ?, ?, ?, ?)"
            self.cursor.execute(sql, (mNo, mMark, mPrice, mNote, mFile))
        except Exception as err:
            print("插入数据错误：", err)

    # 显示数据
    def showDB(self):
        try:
            con = sqlite3.connect("Phones.db")
            cursor = con.cursor()
            print("%-8s %-16s %-8s %-16s %s" % ("No", "Mark", "Price", "Image", "Note"))
            cursor.execute("select mNo, mMsrk, mPrice, mFile, mNote from phones order by mNo")
            rows = cursor.fetchall()
            for row in rows:
                print("%-8s %-16s %-8s %-16s %s" % (row[0], row[1], row[2], row[3], row[4]))
            con.close()
        except Exception as err:
            print("显示错误：", err)

    # 下载
    def download(self, src1, src2, mFile):
        #下载图像，先从src1下载，下载不到时转src2下载
        data = None
        if src1:
            try:
                req = urllib.request.Request(src1, headers=MySpider.headers)
                resp = urllib.request.urlopen(req, timeout=400)
                data = resp.read()
            except:
                pass
        if not data and src2:
            try:
                req = urllib.request.Request(src2, headers=MySpider.headers)
                resp = urllib.request.urlopen(req, timeout=400)
                data = resp.read()
            except:
                pass
        if data:
            fobj = open(MySpider.imagePath + "\\" + mFile, "wb")
            fobj.write(data)
            fobj.close()
            print("download：", mFile)

    # 流程爬虫
    def processSpider(self):
        #global price
        #global mFile
        #爬取一个页面的数据
        try:
            time.sleep(1)   #等待一秒
            print(self.driver.current_url)
            lis = self.driver.find_elements_by_xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
            for li in lis:
                # 我们发现该图像位于src或data-lazy-img属性中.
                try:
                    src1 = li.find_element_by_xpath(".//div[@class='p-img']//a//img").get_attribute("src")
                except:
                    src1 = ""
                try:
                    src2 = li.find_element_by_xpath(".//div[@class='p-img']//a//img").get_attribute("data-lazy-img")
                except:
                    src2 = ""
                try:
                    price = li.find_element_by_xpath(".//div[@class='p-price']//i").text
                except:
                    price = "0"
                try:
                    note = li.find_element_by_xpath(".//div[@class='p-name p-name-type-2']//em").text
                    mark = note.split(" ")[0]
                    mark = mark.replace("爱心东东\n", "")
                    mark = mark.replace(",", "")
                    note = note.replace("爱心东东\n", "")
                    note = note.replace(",", "")
                except:
                    note = ""
                    mark = ""

                self.No = self.No + 1
                no = str(self.No)
                while len(no) < 6:
                    no = "0" + no
                print(no, mark, price)
                #爬取图像地址
                if src1:
                    src1 = urllib.request.urljoin(self.driver.current_url, src1)
                    p = src1.rfind(".")
                    mFile = no + src1[p:]
                elif src2:
                    src2 = urllib.request.urljoin(self.driver.current_url, src2)
                    p = src2.rfind(".")
                    mFile = no + src2[p:]
                if src1 or src2:
                    #启动子线程下载图像
                    T = threading.Thread(target=self.download, args=(src1, src2, mFile))
                    T.setDaemon(False)
                    T.start()
                    self.threads.append(T)
                else:
                    mFile = ""
                self.insertDB(no, mark, price, note, mFile)

            #实现翻页
            try:
                #如果这个无效按钮存在就到最后一页
                self.driver.find_element_by_xpath("//span[@class='p-num']//a[@class='pn-next disabled']")
            except:
                #找到下一页按钮，点击click到下一页
                nextPage = self.driver.find_element_by_xpath("//span[@class='p-num']//a[@class='pn-next']")
                nextPage.click()
                self.processSpider()
        except Exception as err:
            print("爬取过程错误：", err)

    # 执行爬虫
    def executeSpider(self, url, key):
        #爬取函数
        startTime = datetime.datetime.now()
        print("爬虫开始...")
        self.startUp(url, key)
        self.processSpider()
        self.closeUp()
        #等待线程结束
        for t in self.threads:
            t.join()
        print("爬虫完成...")
        endTime = datetime.datetime.now()
        elapsed = (endTime - startTime).seconds
        print("合计（总数）", elapsed, "经过的秒数")


# 主程序
url = "https://www.jd.com"
spider = MySpider()
while True:
    print("1.爬取")
    print("2.显示")
    print("3.退出")
    s = input("请选择（1，2，3）：")
    if s == "1":
        spider.executeSpider(url, "手机")
    elif s == "2":
        spider.showDB()
    elif s == "3":
        break


