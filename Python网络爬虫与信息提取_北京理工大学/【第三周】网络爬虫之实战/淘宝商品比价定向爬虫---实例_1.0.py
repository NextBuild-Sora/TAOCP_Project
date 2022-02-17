
# 淘宝商品比价定向爬虫---实例 #
# --1.0版--

import requests
import re


    
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
        
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("爬虫！！！")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    
    count = 0
    
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
          

# 1、商品信息打印（输出）不出来。。。
# 2、改完代码后就可以了。

 
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)

            headers = {
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", 
                "cookie": "t=a6879c42111c31aac1e333b15089dffd; cna=H0/WF1QUdTcCAd9KOfbRWUme; xlly_s=1; _m_h5_tk=c86d8ec6fbf3d05df9202172d02fb14f_1599058770380; _m_h5_tk_enc=a7b2c6562b3243d17d69fb014e5c7097; cookie2=24ebcaf5756b536b707eabca1e23a12c; v=0; _tb_token_=e53b6ee3b3376; _samesite_flag_=true; sgcookie=E100b6pQQnfrSr4RmhZ1Hvi55czY8c5JVpr%2F4yTI2l4EPfmOW18DKe9M%2BM6W8c9ZezFGlB6FWFN7PIVhmHDHPww%2F4w%3D%3D; unb=3486941668; uc3=id2=UNQ%2F0BPPxt1CNw%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dCufXGAxLt3vHEDQ4%3D&nk2=q%2FLBjK7YcPJ5fBT9XQ58xg%3D%3D; csg=f1b760ee; lgc=%5Cu5168%5Cu9762%5Cu5E73%5Cu8861%5Cu5145%5Cu5206%5Cu53D1%5Cu5C55; cookie17=UNQ%2F0BPPxt1CNw%3D%3D; dnk=%5Cu5168%5Cu9762%5Cu5E73%5Cu8861%5Cu5145%5Cu5206%5Cu53D1%5Cu5C55; skt=800f5847ebc8cc97; existShop=MTU5OTA1MjM2OA%3D%3D; uc4=nk4=0%40qUfIoDPPEAR24hwY%2B7uqzkXlxKt4UBNm7wP0&id4=0%40UgP0BY3mjw1jNCaGQd23TrtWkIJs; tracknick=%5Cu5168%5Cu9762%5Cu5E73%5Cu8861%5Cu5145%5Cu5206%5Cu53D1%5Cu5C55; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%B1%958b; _nk_=%5Cu5168%5Cu9762%5Cu5E73%5Cu8861%5Cu5145%5Cu5206%5Cu53D1%5Cu5C55; cookie1=WqJ84kG6PHakwC0HvrIXdN63tSwdwj33TvE4UGrqj1w%3D; mt=ci=37_1; thw=cn; enc=iVmFhTO83FjMUos1rFCfrxQpl0AlNvA3poJtCN%2Bk7Hm5BnUGECkogmuSh0%2F4GG8oaBmrDAknIaFDLfsLRLMm7g%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=DC4F9343DC4D858BA1413E638262789B; uc1=cookie21=U%2BGCWk%2F7pY%2FF&cookie14=UoTV5YzY%2F5GHvQ%3D%3D&existShop=false&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&pas=0&cookie15=WqG3DMC9VAQiUQ%3D%3D; tfstk=c82PBNA4ETBPxKkC6YMed4UeUsJRZJln_KoKZWmt8CK2q7cliQ8Km-Yt0c3Onbf..; l=eBEN5AtmOsv3sRyBBO5aPurza779iIRb8sPzaNbMiInca6GP6FTAwNQ4tH2MJdtjgtfvmFxPDcnX3Ree8SaLREgKqelrgnspBxJ9-; isg=BICAcV22ywwWCrcIyx2w9xQEUQ5SCWTT22W2FvoR9hsudSKfpBiVY_EHjd21RRyr"
                    }   # cookie 是扫描登陆的，可能会失效。
            
            #html = getHTMLText(url)    #这行代码是否删除，都可以，看样子不影响运行结果。
            html = requests.get( url, headers=headers )
            #print ( html.text )    #打印爬取的网页内容。
            parsePage(infoList, html.text )
        except:
            continue
    printGoodsList(infoList)
   
main()

