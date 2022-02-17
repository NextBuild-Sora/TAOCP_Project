
#----------Requests库7个的主要方法------------#

#********************************************************************#
"""
    requests.request() :构造一个请求，支撑以下各方法的基础方法.
    requests.get() :获取HTML网页的主要方法，对应于HTTP的GET。
    requests.head()：获取HTML网页头信息的方法，对应于HTTP的HEAD。
    requests.post() ：向HTML网页提交POST请求的方法，对应于HTTP的POST 。
    requests.put()：向HTML网页提交PUT请求的方法，对应于HTTP的PUT。
    requests.patch() 向HTML网页提交局部修改请求，对应于HTTP的PATCH 。
    requests.delete() 向HTML页面提交删除请求，对应于HTTP的DELETE。

"""
#********************************************************************#


import requests

r = requests.head( 'https://www.baidu.com' )
q = r.headers   #获取网页头部信息。
print ("头部信息：", q)

q1 = r.text
print( "网页内容：" , q1 )


