

# --------------- 中国大学排名定向爬虫 --------------- #

import requests
from bs4 import BeautifulSoup
import bs4 

def getHTMLText(url):
    try:
        r = requests.get(url , timeout = 30 )
        r.raise_for_ststus()    # ststus()单词拼错；正确的是：status()。难怪运行总异常。
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "



def fillUnivList( ulist , html ):
    soup = BeautifulSoup( html , "html.parser" )
    for tr in soup.find( 'tbody' ).children:
        if isinstance( tr, bs4.element.Tag ):
            tds = tr('td')
            ulist.append( [tds[0].string, tds[1].string, tds[3].string ] )


def printUnivList( ulist , num ):
    print ( '{:^10}\t{:^6}\t{:^10}'.format( "排名", "学校名称", "总分" ) )
    for i in range( num ):
        u = ulist[ i ]
        print ( "{:^10}\t{:^6}\t{:^10}".format( u[0], u[1], u[2] ) )
    
def main():
    uinfo = [ ]
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"  #这里要 ‘http’ 才行，‘https’ 会运行异常。
    html = getHTMLText( url )
    fillUnivList( uinfo, html )
    printUnivList( uinfo, 20 ) # 20位.

main( )


