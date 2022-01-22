
#执行程序

from scrapy import cmdline

#执行命令; 其中mySpider就是我们爬虫程序的名称，后面的参数是不显示调试信息。
cmdline.execute("scrapy crawl mySpider -s LOG_ENABLED=False".split())


