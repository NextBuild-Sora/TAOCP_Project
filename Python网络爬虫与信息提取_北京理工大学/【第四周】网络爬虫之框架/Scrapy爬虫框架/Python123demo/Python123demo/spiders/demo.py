import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['python123.io']     #可选; 允许_域名。
    start_urls = ['http://python123.io/ws/demo.html']   #开始链接。

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open( fname, 'wb' ) as f:
            f.write( response.body )
        self.log( 'Saved file %s.' % fname )
