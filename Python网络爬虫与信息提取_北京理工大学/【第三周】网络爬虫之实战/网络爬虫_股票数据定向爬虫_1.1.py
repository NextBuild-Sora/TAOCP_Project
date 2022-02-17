

# -------- 股票数据定向爬虫 -------- #
# ---实例----、
# --1.1版--
# 如何提高用户体验？


import requests
from bs4 import BeautifulSoup
import traceback
import re

#速度提高：编码识别优化。
def getHTMLText(url , code = "utf-8"):   
    try:
        r = requests.get( url ) 
        r.raise_for_status() 
        r.encoding = code 
        return r.text
    except:
        return " "

def getStockList(lst, stockURL ): 
    html = getHTMLText( stockURL, "GB2312" )
    soup = BeautifulSoup( html , 'html.parser' )
    a = soup.find_all( 'a' )
    for i in a:
        try:
            href = i.attrs['href']
            lst.append( re.findall( r"[s][hz]\d{6}", href )[0] )
        except:
            continue

#体验提高：增加动态进度显示。
def getStockInfo( lst , stockURL, fpath ):
    count = 0

    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText( url )
        try:
            if html == " ":
                continue
            infoDict = { }      #信息字典
            soup = BeautifulSoup( html, "html.patser" )
            stockInfo = soup.find( 'div', atttrs = {'class':'stock-bets'} )

            name = stockInfo.find_all( attrs = {'class':'bets-name'} )[0]
            infoDict.update( {'股票名称': name.text.split()[0]} )

            keyList = stockInfo.find_all( 'dt' )
            valueList = stockInfo.find_all( 'dd' )
            for i in range( len(keyList) ):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
        
            with open( fpath, 'a', ecoding = 'utf-8' ) as f:
                f.writ( str(infoDict) + '\n' )
                count = count + 1
                print ( '\r当前进度：{:.2f}%' .format(count*100/len(lst)) , end = "" ) 
        except:
            count = count + 1
            print ( '\r当前进度：{:.2f}%' .format( count*100/len(lst) ) , end = "" ) 
            # traceback.print_exc()
            # continue

           


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'    #股票—列表
    #stock_info_url = 'https://gupiao.baidu.com/stock/'      #股票-信息
    stock_info_url = 'https://www.laohu8.com/stock/'

    output_file = 'D://BaiduStockInfo.txt'      #输出-文件
    slist = []
    getStockList( slist , stock_list_url )
    getStockInfo( slist , stock_info_url , output_file )

main()

