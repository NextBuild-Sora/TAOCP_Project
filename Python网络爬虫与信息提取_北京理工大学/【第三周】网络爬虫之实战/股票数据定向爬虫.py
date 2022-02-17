

# -------- 股票数据定向爬虫 -------- #
# ---实例----、
# --1.0版--


import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("1")
        return ""
 
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'\d{6}',href))
        except:
            print("2")
            continue
 
 
def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        if stock == []:
            continue
        else:
            url = stockURL + stock[0]
            html = getHTMLText(url)
            try:
                if html == "":
                    continue
                infoDict = {}
                soup = BeautifulSoup(html, 'html.parser')
                stockInfo = soup.find('div', attrs={'class': 'detail-data'})
                name = soup.find_all(attrs={'class': 'name'})[0]
                infoDict.update({'股票名称': name.text.split()[0]})
 
                keyList = stockInfo.find_all('dt')
                valueList = stockInfo.find_all('dd')
                for i in range(len(keyList)):
                    key = keyList[i].text
                    val = valueList[i].text
                    infoDict[key] = val
 
                with open(fpath, 'a', encoding='utf-8') as f:
                    f.write(str(infoDict) + '\n')
            except:
                print("3")
                traceback.print_exc()
                continue
 
def main():
    stock_list_url = 'https://www.banban.cn/gupiao/list_sh.html'
    stock_info_url = 'https://www.laohu8.com/stock/'
    output_file = 'D:/老虎StockInfo.txt'
    output_file = 'D:/老虎StockInfo.xls'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()