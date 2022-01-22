#**********************************
#
# 爬取58同城网站招聘信息
#
#**********************************


from selenium import webdriver
import sqlite3
import time

class MySpider:
    def __init__(self):
        # 指定chrome.exe绝对路径。设置binary_location属性:
        options = webdriver.ChromeOptions()
        options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
        self.chrome = webdriver.Chrome(options=options)


    def openDB(self):
            self.con = sqlite3.connect("爬取58同城网站招聘信息.db")
            self.cursor = self.con.cursor()

    def initDB(self):
        try:
            self.cursor.execute("drop table 爬取58同城网站招聘信息")
        except:
            pass
        self.cursor.execute("create table 爬取58同城网站招聘信息 (company varchar(256),\
            occupation varchar(256),address varchar(256),\
                     require varchar(256),salary varchar(128),\
                     primary key (company,occupation))")
        self.count = 0
        self.inserted = 0

    def closeDB(self):
        self.con.commit()
        self.con.close()
        self.chrome.close()

    def spider(self):
        try:
            time.sleep(2)
            print(self.chrome.current_url)

            lis = self.chrome.find_element_by_id("list_con").find_elements_by_xpath(".//li[@class='job_item clearfix']")
            for li in lis:
                try:
                    company = li.find_element_by_xpath(".//div[@class='comp_name']//a").text
                except:
                    company = ""
                try:
                    address = li.find_element_by_xpath( ".//span[@class='address']" ).text
                except:
                    address = ""
                try:
                    occupation = li.find_element_by_xpath(".//span[@class='name']").text
                except:
                    occupation = ""
                try:
                    salary = li.find_element_by_xpath(".//p[@class='job_salary']").text
                except:
                    salary = ""
                try:
                    require = li.find_element_by_xpath(".//p[@class='job_require']").text
                except:
                    require = ""

                self.count += 1

                if company !="":
                    try:
                        sql = "insert into 爬取58同城网站招聘信息(company,occupation,address,require,salary) values (?,?,?,?,?)"
                        self.cursor.execute(sql, (company,occupation,address,require,salary))
                        self.inserted += 1
                    except:
                        print("----------", company + " 已经存在")
                print(self.inserted, "/", self.count, company, salary)
            try:
                link = self.chrome.find_element_by_xpath("//div[@class='pagesout']//a[@class='next']")
                link.click()
                self.spider()
            except:
                pass

        except Exception as err:
            print("爬取错误：", err)

    def show(self):
        self.cursor.execute("select company, occupation,address,require,salary from 爬取58同城网站招聘信息")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4])
        print('总数', len(rows))


spider = MySpider()
spider.openDB()
while True:
    print(" 1.爬取 ")
    print(" 2.显示 ")
    print(" 3.退出 ")
    s = input("选择（1，2，3）：")

    if s == "1":
        spider.initDB()
        spider.chrome.get("https://sz.58.com/ruanjiangong/?PGTID=0d202408-0000-4643-ad88-f906f70cbce9&ClickID=1")
        spider.spider()
    elif s == "2":
        spider.show()
    elif s == "3":
        break

spider.closeDB()



