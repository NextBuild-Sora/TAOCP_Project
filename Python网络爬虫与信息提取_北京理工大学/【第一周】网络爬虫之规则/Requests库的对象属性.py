
# Requests对象的属性
#****************************************************************#
'''
    r.status_code : HTTP请求的返回状态，200表示连接成功，404表示失败.
    r.text : HTTP响应内容的字符串形式，即，url对应的页面内容 .
    r.encoding : 从HTTP header中猜测的响应内容编码方式.
    r.apparent_encoding : 从内容中分析出的响应内容编码方式（备选编码方式）.
    r.content : HTTP响应内容的二进制形式.
    
'''
#****************************************************************#

import requests

r1 = requests.get( "https://www.baidu.com" )

p = r1.status_code 
print("状态编码：", p)
print()
p1 =  r1.text 
print ("文本内容：", p1)
print()

#从HTTP header中猜测的响应内容编码方式：
p2 = r1.encoding    
print("内容编码：", p2)
print()

#根据内容分析出的响应内容编码方式（备选编码方式）：
p3 = r1.apparent_encoding   
print("显示内容编码（备选）：" , p3)
print()

r1.encoding = "uft-8"   #内容编码转换为utf-8.
print()

哦 = r1.text
print ("文本内容：" , 哦)

print ()

