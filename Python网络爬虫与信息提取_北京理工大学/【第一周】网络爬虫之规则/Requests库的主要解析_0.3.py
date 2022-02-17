
#----------Requests库的主要方法解析------------#


# --0.3版--


#*************************************************************#
'''

        requests.request(method, url, **kwargs)
    ∙ method : 请求方式，对应get/put/post等7种.
    ∙ url: 拟获取页面的url链接. 
    ∙ **kwargs: 控制访问的（可选）参数，共13.
---------------------------------------------
'''
#*************************************************************#

import requests

print()

# files: 字典类型，传输文件.
fs = { 'file': open( "D:\文档\Python文件\Python网络爬虫与信息提取\DATA工作表.xlsx", 'rb' ) }
r = requests.request( 'post' , 'http://python123.io/ws' , files = fs )
print ( "文件：", r )

print()

# timeout : 设定超时时间，秒为单位.
r1 = requests.request( 'get', 'http://www.baidu.com', timeout = 10 )
print( "timeout（超时）：", r1 )

print()

# proxies : 字典类型，设定访问代理服务器，可以增加登录认证.
pxs = { 'http' : 'http://user:pass@10.10.10.1:1234' ,
        'https' : 'https://10.10.10.1:4321' }
r2 = requests.request('GET', 'http://www.baidu.com', proxies = pxs)
print ( "访问代理：", r2 )

print()

