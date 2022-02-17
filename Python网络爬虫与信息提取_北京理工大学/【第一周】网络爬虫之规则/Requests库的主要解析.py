
#----------Requests库的主要方法解析------------#

#********************************************************************#
'''

    GET 请求获取URL位置的资源. 
    HEAD 请求获取URL位置资源的响应消息报告，即获得该资源的头部信息. 
    POST 请求向URL位置的资源后附加新的数据.
    PUT 请求向URL位置存储一个资源，覆盖原URL位置的资源. 
    PATCH 请求局部更新URL位置的资源，即改变该处资源的部分内容. 
    DELETE 请求删除URL位置存储的资源.

'''
#********************************************************************#

# --0.1版--


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
        params : 字典或字节序列，作为参数增加到url中
                ..............              
'''
#*************************************************************#

import requests

print()

# params : 字典或字节序列，作为参数增加到url中：
kv = {'key1':'value1' , 'key2':'valuue2'}
r = requests.request( 'get', 'http://python123.io/ws' , params = kv )
print ( r.url )

print()