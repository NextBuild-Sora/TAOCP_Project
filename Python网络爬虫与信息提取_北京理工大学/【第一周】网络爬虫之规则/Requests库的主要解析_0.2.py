
#----------Requests库的主要方法解析------------#


# --0.2版--


#*************************************************************#
'''

        requests.request(method, url, **kwargs)
    ∙ method : 请求方式，对应get/put/post等7种.
    ∙ url: 拟获取页面的url链接. 
    ∙ **kwargs: 控制访问的参数，共13.
---------------------------------------------
    ∙ method : 请求方式 r = requests.request('GET', url, **kwargs) 
    r = requests.request( 'HEAD', url, **kwargs ) 
    r = requests.request( 'POST', url, **kwargs ) 
    r = requests.request( 'PUT', url, **kwargs ) 
    r = requests.request( 'PATCH', url, **kwargs ) 
    r = requests.request( 'delete', url, **kwargs ) 
    r = requests.request( 'OPTIONS', url, **kwargs )
-------------------------------------------------------
    ∙ **kwargs: 控制访问的参数，均为可选项 
        
                ..............              
'''
#*************************************************************#

import requests

print()

# data 字典、字节序列或文件对象，作为Request的内容：
kv = {'key1':'value1' , 'key2':'valuue2'}
r = requests.request( 'post', 'http://python123.io/ws' , data = kv )
print ( 'date对象：', r )

print()

body = "ZhuTiNeiRong"
r = requests.request('post' , 'http://python123.io/ws' , data = body )
print( "DATA对象：", r )

print()

# json：JSON格式的数据，作为Request的内容
k1 = {'key1':'value1'}
r2 = requests.request('POST' , 'http://python123.io/ws' , json = k1 )
print ( "JSON数据：", r2 )

print()

# headers : 字典，HTTP定制头
hd = {'user-agent':'Chrome/10' }
r3 = requests.request('post', 'http://python123.io/ws', headers = hd )
print ( "头部：", r3 )

