
#爬虫程序

import scrapy

class MySpider(scrapy.Spider):
    name = "mySpider"

    def start_requests(self):
        url = 'http://127.0.0.1:5000'
        yield scrapy.Request(url= url, callback= self.parse)

    def parse(self, response):
        print(response.url)
        data = response.body.decode()   #二进制数据的网页；解码成为字符串。
        print(data)


