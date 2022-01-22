

# ---- 2.6 实践项目－爬取天气预报数据 ---- #

#编写爬取的程序爬取深圳7天的天气预报数据：

from bs4 import BeautifulSoup 
from bs4 import UnicodeDammit   #自动识别网站编码的模块
import urllib.request

url=url="http://www.weather.com.cn/weather/101280601.shtml"
try:
    headers={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
    req=urllib.request.Request(url, headers=headers)
    data=urllib.request.urlopen(req)
    data=data.read()
    
    dammit=UnicodeDammit(data, ["utf-8","gbk"])
    data=dammit.unicode_markup
    soup=BeautifulSoup(data, "lxml")
    lis=soup.select("ul[class='t clearfix'] li")

    for li in lis:
        try:
            date=li.select('h1')[0].text
            weather=li.select('p[class="wea"]')[0].text
            temp=li.select('p[class="tem"] span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
            print(date, weather, temp)
        except Exception as err:
            print("捕捉到错误信息：", err)
except Exception as e:
    print("最终错误信息：", e)

    



