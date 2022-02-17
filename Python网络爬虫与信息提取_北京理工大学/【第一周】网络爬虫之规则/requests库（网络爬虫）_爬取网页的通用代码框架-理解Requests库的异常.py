
# requests库（网络爬虫）__爬取网页的通用代码框架 --------------- #
# ---- 理解Requests库的异常 ----

# *************************************************************** #
''' 
    r.raise_for_status()在方法内部判断r.status_code是否等于200，
                不需要 增加额外的if语句，
                该语句便于利用try‐except进行异常处理    
'''
# ************************************************************** #


import requests

#T = input ( "getHTMLText：")
def getHTMLText( url ) : 
    try:
        r = requests.get( url , timeout = 30 )
        r.raise_for_status()   #如果状态不是200，引发HTTPError异常。
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " 产生异常 "

if __name__ == "_main_" :
    url = "https://www.baidu.com"
    print ( getHTMLText( url ) )

if __name__ == "_main_" :
    url = "www.baidu.com"
    print ( getHTMLText( url ) ) 

############################################    
'''
r = requests.get("www.baidu.com")
print ( r.status_code )

a = r.text
print ( getHTMLText )
'''
############################################


#------------------------------------------------------------------------#
'''
    requests.ConnectionError ：网络连接错误异常，如DNS查询失败、拒绝连接等 。
    requests.HTTPError ：HTTP错误异常。
    requests.URLRequired：URL缺失异常。
    requests.TooManyRedirects ：超过最大重定向次数，产生重定向异常。
    requests.ConnectTimeout ： 连接远程服务器超时异常 。
    requests.Timeout：请求URL超时，产生超时异常。

'''
#------------------------------------------------------------------------#

