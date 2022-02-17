

# -------- 股票数据定向爬虫 -------- #
# ---实例----、

#************************************************************************#
'''
    ---功能描述---
    目标：获取上交所和深交所所有股票的名称和交易信息。 
    输出：保存到文件中。

        技术路线：requests‐bs4‐re。
-----------------------------------------------------

    ---候选数据网站的选择---

    新浪股票：http://finance.sina.com.cn/stock/ 。
    百度股票：https://gupiao.baidu.com/stock/ 。
    ----百度股票网站已关闭。----
    
    选取原则：股票信息静态存在于HTML页面中，非js代码生成 、；没有Robots协议限制
    选取方法：浏览器 F12，源代码查看等 选取心态：不要纠结于某个网站，多找信息源尝试
-------------------------------------------------------------------
    获取股票列表： 
    东方财富网：http://quote.eastmoney.com/stocklist.html 
    获取个股信息： 百度股票：https://gupiao.baidu.com/stock/ 
    单个股票：https://gupiao.baidu.com/stock/sz002439.html
     
------------------------------------------------------------------------
    ---程序的结构设计---
    步骤1：从东方财富网获取股票列表 
    步骤2：根据股票列表逐个到百度股票获取个股信息 
    步骤3：将结果存储到文件

'''
#************************************************************************#

import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    return ''

def getStockList(lst, stockURL ): 
    return ''

def getStockInfo( lst , stockURL, fpath ):
    return ''

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    # stock_info_url = 'https://gupiao.baidu.com/stock/'
    stock_info_url = 'https://www.laohu8.com/stock/'
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    getStockList(slist , stock_list_url )
    getStockInfo( slist , stock_info_url )

main()

