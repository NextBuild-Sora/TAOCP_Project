

# -*- 爬取与储存天气预报数据 -*-
# -0.2-


"""
    我们可以获取北京、上海、广州、深圳等城市的代码，爬取这些城
市的天气预报数据，并存储到sqllite数据库weathers.db中，存储
的数据表weathers是：
    create table weathers (wCity varchar(16),wDate
varchar(16),wWeather varchar(64),wTemp
varchar(32),constraint pk_weather primary key 
(wCity,wDate))

"""


from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import sqlite3

class WeatherDB:    #对数据库的操作
    def openDB(self):   #打开
        self.con=sqlite3.connect("weathers.db")
        self.cursor=self.con.cursor()
        try:    #打开openDB的时候，首先创建好这个表格；注意：第一次创建是成功的。
            self.cursour.execute("create table weathers (wCity varchar(16), wDatevarchar(16), wWeather varchar(64), wTemp varchar(32), constraint pk_weatherprimary key (wCity,wDate))")
        except:     #第二次创建是不成功的，产生一个异常。
            self.cursor.execute("delete from weathers")     #在这个异常下，先把表格清空；这个表格是空的。
    
    def closeDB(self):  #关闭
        self.con.commit()
        self.con.close()

    def insert(self, city, date, weather, temp):    #插入一条记录
        try:
            self.cursor.execute("insert into weathers (wCity,wDate,wWeather,wTemp) values (?,?,?,?)" ,(city,date,weather,temp))        
        except Exception as err:
            print("捕捉错误信息：", err)
    
    def show(self):     #虚无函数用来显示使用的记录；在这个数据库查找到所有的行并对这个行进行显示
        self.cursor.execute("select * from weathers")
        rows=self.cursor.fechall()
        print("%-16s%-16s%-32s%-16s" % ("city","date","weather","temp")) 
        for row in rows:
            print("%-16s%-16s%-32s%-16s" % (row[0],row[1],row[2],row[3]))   #格式化的方式进行显示
           
class WeatherForecast:  #调用url的“请求”函数去访问网站。
    def __init__(self):
        self.headers={
            "User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
        self.cityCode={"北京":"101010100","上海":"101020100","广州":"101280101","深圳":"101280601"}     #要查找天气的城市。

    def forecastCity(self, city):   #循环city找到city的库
        if city not in self.cityCode.keys():
            print(city+"code cannot be found")
            return
        
        url="http://www.weather.com.cn/weather/" + self.cityCode[city] + ".shtml"
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
            req = urllib.request.Request(url, headers=headers)
            data = urllib.request.urlopen(req)
            data = data.read()
    
            dammit = UnicodeDammit(data, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            soup = BeautifulSoup(data, "lxml")
            lis = soup.select("ul[class='t clearfix'] li")
    
            n = 0
            for li in lis:
                try:
                    date = li.select('h1')[0].text
                    weather = li.select('p[class="wea"]')[0].text
    
                    if n > 0:
                        temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
                    else:
                        temp = li.select('p[class="tem"] i')[0].text
    
                    print(city, date, weather, temp)    #显示天气
                    self.db.insert(city, date, weather, temp)
                    n = n + 1
                except Exception as err:
                    print("捕捉到错误信息：", err)
        except Exception as e:
            print("最终错误信息：", e)

    def process(self, cities):  #process程序启动的时候创建一个DB
        self.db=WeatherDB()     
        self.db.openDB()
        
        for city in cities:     #查找城市的天气
            self.forecastCity(city)
            
        #self.db.show()
        self.db.closeDB()   #放置城市天气，放进数据库里面。
            
ws = WeatherForecast()
ws.process( ["北京", "上海", "广州", "深圳"] )
print( "completed" )



    