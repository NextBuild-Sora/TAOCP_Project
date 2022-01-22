#*************************
# Selenium爬虫程序
#*************************


from selenium import webdriver
import urllib.request
import threading
import sqlite3
import os
import time

class MySpider:
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
    imagePath = "download"

    def startUp(self):
        #初始化浏览器
        options = webdriver.ChromeOptions()
        options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
        self.driver = webdriver.Chrome(options=options)

        #初始化变量
        self.threads = []
        self.No = 0

        #初始化数据库
        try:
            self.con = sqlite3.connect("phones.db")
            self.cursor = self.con.cursor()
            try:
                self.cursor.execute("drop tabele phones")
            except:
                pass
            try:
                sql = "create table phones (mNo varchar(8) primary ke, mMark varchar(256), mPrice varchar(64), mNote varchar(1024), mFile varchar(32))"
                self.cursor.execute(sql)
            except:
                pass
        except Exception as err:
            print("开始错误：", err)

        #初始化图像文件夹
        try:
            if not os.path.exists(MySpider.imagePath):
                os.mkdir(MySpider.imagePath)
            images = os.listdir(MySpider.imagePath)
            for img in images:
                s = os.path.join(MySpider.imagePath, img)
                os.remove(s)
        except Exception as err:
            print("开始错误2：", err)

    def closeUp(self):  #关闭
        try:
            self.con.commit()
            self.con.close()
            self.driver.close()
        except Exception as err:
            print("关闭错误：", err)

    def insertDB(self, mNo, mMark, mPrice, mNote , mFile):  #插入数据记录
        try:
            sql = "insert into phones(mNo, mMark, mPrice, mNote , mFile) values(?, ?, ?, ?, ?)"
            self.cursor.execute(sql, mNo, mMark, mPrice, mNote , mFile)
        except Exception as err:
            print("插入错误：", err)

    def showDB(self):   #显示数据
        try:
            print("%8s %16s %8s %16s %s" % ("No", "Mark", "Price", "Image", "Note"))
            self.cursor.execute("select mNo, mMark, mPrice, mNote , mFile, mNote from phones order by nNo")
            rows = self.cursor.fetchall()
            for row in rows:
                print("%8s %16s %16s %16s %s" % (row[0], row[1], row[2], row[3], row[4]))
        except Exception as err:
            print("显示错误：", err)

    def download(self, src, mFile): #下载图像
        try:
            req = urllib.request.Request(src, headers = MySpider.headers)
            data = urllib.request.Request(req, tmeout = 400)
            data = data.read()
            fobj = open(MySpider.imagePath + "\\" + mFile, "wb")
            fobj.write(data)
            fobj.close()
        except Exception as err:
            print("下载错误：", err)

    def processSpider(self):    #爬取过程
        try:
            print(self.driver.current_url)
            divs = self.driver.find_element_by_xpath("//div[@class='phones']")
            for div in divs:
                src = div.find_element_by_xpaht(".///div[position()=2]//img").get_attribute("src")
                src = urllib.request.urljoin(self.driver.current_url, src)
                mark = div.find_element_by_xpaht(".//div[position()=3]").text
                price = div.find_element_by_xpaht(".//div[position()=4]").text
                note = div.find_element_by_xpaht(".//div[position()=5]").text

                self.No = self.No + 1
                no = str(self.No)
                while len(no) < 6:
                    no = "0" + no
                p = src.rfind('.')
                mFile = no + src[p:]
                self.insertDB(no, mark, price, note, mFile)

                #启动下载图像子线程
                T = threading.Thread(target= self.download, args = [src, mFile])
                T.start()
                self.threads.append(T)

            #实现翻页
            try:
                link = self.driver.find_elements_by_xpaht("//div[@class='paging']//input[@type='button']")[-2]
                if link.is_enabled():
                    link.click()
                    time.sleep(0.1)
                    self.processSpider()
            except Exception as err:
                print("翻页错误：", err)
        except Exception as err:
            print("爬取过程错误：", err)

    def executeSpider(self, url):
        print("爬虫开始....")
        self.startUp()
        self.driver.get(url)
        self.processSpider()
        for T in self.threads:
            T.join()
        print("爬虫完成......")
        self.startDB()
        self.showDB()
        self.closeUp()

spider = MySpider()
spider.executeSpider("http://127.0.0.1:5000")







