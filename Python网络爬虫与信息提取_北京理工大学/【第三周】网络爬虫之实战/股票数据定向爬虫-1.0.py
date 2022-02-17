

# -------- 股票数据定向爬虫-1 -------- #
# 其他同学的代码--


import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL) #首先使用getHTMLText获取页面
    soup = BeautifulSoup(html, 'html.parser') #使用BeautifulSoup库解析页面
    a = soup.find_all('a') #找到页面中的所有a标签
    for i in a: #对所有a标签进行遍历，进行处理
        try:
            href = i.attrs['href']
            s = (re.findall(r"[s][hz]/\d{6}", href)[0]) #以s开头，中间是h或z字符，然后是/和六个数字
            s = s[3:] #由于中财网的链接只需要六个数字 所以只提取六位数字即可
            if s not in lst: #防止重复获取相同的信息
                lst.append(s) #在所有a标签中寻找符合条件的信息并保存在列表中
            else:
                continue
        except:
            continue #如果不符合则继续运行程序
         
 
def getStockInfo(lst, stockURL, fpath):
    lst.remove('000018') #由于页面编码完全不同 所以去除了两个此代码无法爬取的个股页面
    lst.remove('000022')
    for stock in lst: #对每一支个股页面发起访问请求
        url = stockURL + stock + ".html" #用中财链接加我们刚才获得的个股链接，形成每一支个股的URL
        html = getHTMLText(url) #使用函数访问URL并保存在demo中
        try:
            if html == "": #如果页面为空 则跳过
                continue
            infoDict = {} #定义一个字典来保存个股信息
            soup = BeautifulSoup(html, 'html.parser') #用BeautifulSoup库来构建解析网页的类型
            stockInfo = soup.find('div',attrs = {'id':'act_quote'}) #找到股票信息的总头 是div开头的 id=act_quote的标签信息
            name = stockInfo.find_all(attrs = {'class':'tit01'})[0] #在股票信息中查找股票名称信息 这条信息存在class='tit01'中
            infoDict.update({'股票名称':name.text}) #将股票名称存入字典 因为我们的源代码中股票名称没有别的多余字符 所以可以省略split步骤
            Info = soup.find('td',attrs = {'class':'Rlist'}) #个股页面信息都存在class="Rlist"中
            Infols = []
            for i in Info.find_all('td'): #搜索每一条td信息
                Infols.append(i.text) #将个股所有信息放入列表
            with open(fpath, 'a', encoding = 'utf-8') as f:
                f.write('\n\n' + str(infoDict) + '\n')
                for i in Infols:
                    f.write(str(i)+'\n')
        except:
            traceback.print_exc()
            print(url)
            continue
             
             
 
def main():
    stock_list_url = 'https://www.yz21.org/stock/info/' #获取股票列表网站
    stock_info_url = 'https://quote.cfi.cn/' #获取个股信息网站
    output_file = 'D:\网络爬虫篇\股票数据定向爬虫\股票信息.txt' #输出文件位置
    slist = []
    getStockList(slist, stock_list_url) #调用函数获取股票列表
    getStockInfo(slist, stock_info_url, output_file) #根据股票列表到相关网站上获取股票信息并保存到文件中
 
main()