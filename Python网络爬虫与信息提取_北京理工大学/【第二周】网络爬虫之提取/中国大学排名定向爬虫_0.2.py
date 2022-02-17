

# --------------- 中国大学排名定向爬虫 --------------- #
#-----0.2版-----

import requests
from bs4 import BeautifulSoup
import bs4 


def getHTMLText(url):
    try:
        r = requests.get(url , timeout = 30 )
        r.raise_for_status()    #一直运行出错，原来是单词拼错了。
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

'''
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
'''


def fillUnivList( ulist , html ):
    soup = BeautifulSoup( html , "html.parser" )
    for tr in soup.find( 'tbody' ).children:
        if isinstance( tr, bs4.element.Tag ):
            tds = tr('td')
            ulist.append( [tds[0].string, tds[1].string, tds[3].string ] )


def printUnivList( ulist , num ):
    tpil = "{0:^10}\t{1:{3}^10}\t{2:^10}"   #优化中文排版。
    print ( tpil.format( "排名", "学校名称", "总分" , chr(12288)) ) #优化中文排版。
    for i in range( num ):
        u = ulist[ i ]
        print ( tpil.format( u[0], u[1], u[2] , chr(12288)) ) #优化中文排版。
    
def main(): 
    uinfo = [ ]
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"
    #url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText( url )
    fillUnivList( uinfo, html )
    printUnivList( uinfo, 20 ) # 20位.

main( )


