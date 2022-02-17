
# 淘宝商品比价定向爬虫---实例

#-------------------------------------------------------#S
'''
    ---功能描述---
    
    目标：获取淘宝搜索页面的信息，提取其中的商品名称和价格.
    
        理解：
        淘宝的搜索接口 翻页的处理.

    技术路线：requests‐bs4‐re.

------------------------------------------------
    ---- 程序的结构设计 ----
    
    步骤1：提交商品搜索请求，循环获取页面.
    步骤2：对于每个页面，提取商品名称和价格信息.
    步骤3：将信息输出到屏幕上.
'''
#-------------------------------------------------------#


import requests
import re


def getHTMLText(url):
    
    try:
        r = request.get(url, timeout = 30 )
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    
    except:
        return " "


def parsePage(ilt , html ):
    
    try:
        plt = re.findall( r' \"view_price\"\:"[\d\.]*\" ' , html )
        tlt = re.findall( r' \"raw_title"\:\".*?\" ' , html )
        for i in range( len(plt) ):
            price = eval( plt[i].split(':')[1] )    #商品名字。
            title = eval( tlt[i].split(':')[1] )    #商品价格。
            ilt.append( [price , title] )     #后面添加商品的名字和价格。
            
    except:
        print (" ")


def printGoodsList( ilt ):
    
    tplt = "{:4} \t {:8} \t {:16}"  #每个槽的长度进行限制。
    print ( tplt.format( "序号", "价格", "商品名称" ))
    count = 0   #计算总数。
    
    for g in ilt:
        count = count + 1
        print ( tplt.format( count, g[0], g[1] ) )


def main():
    
    goods = '书包'    #商品。
    depth = 3   #深度（页面）。
    start_url = 'https://s.taobao.com/search?q=' + goods    #开始URL.
    infoList = []   #信息（统计）列表。
    
    for i in range( depth ):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage( infoList, html )
            
        except:     #异常处理，对于爬取网页出现的错误进行跳过。
            continue
        # print ( '爬取错误' )
        
    printGoodsList(infoList)


main( )


        
        
