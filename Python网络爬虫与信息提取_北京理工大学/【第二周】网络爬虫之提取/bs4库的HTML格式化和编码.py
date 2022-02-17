
# --------- bs4库好HTML格式化和编码 ------------ #

# --------- 基于bs4库的HTML格式输出：

import requests
r = requests.get( "https://python123.io/ws/demo.html" )
demo = r.text
# print (demo)

# 让HTML内容更加“友好”的显示（HTML的格式化）： bs4 库的 prettify() 方法。

from bs4 import BeautifulSoup

soup = BeautifulSoup( demo, "html.parser" )

a1 = soup.prettify()     #美化
print ( "美化：", a1)


#----------------------------------------------
'''
    .prettify()为HTML文本<>及其内容增加更加'\n' 
    .prettify()可用于标签，方法：<tag>.prettify()
'''
#----------------------------------------------


#****-------------------------------------------------
'''
b = soup.a.perttify()
print ( "soup.a 网页内容标签美化：" , b )

Python解释器运行不会报错，不知为何这里报错了。。。
'''
#****-------------------------------------------------

print ("==============================================")

print ( soup.a.prettify() ) #从Python解释器复制过来，运行正常。。。。

print ("+++++++++++++++++++++++++++++++++++++++++++++++")

print (soup.a.prettify()) #在这敲代码一遍，运行正常。。

print ('##################################################')

b = soup.a.prettify() #在试一试，运行正常。
print (b)

print()
print ("||||||||||||||||||||||||||||||||||||||||||||||||||||")


#*************************************************
'''
    bs4库的编码 ：
    bs4库将任何HTML输入都变成utf‐8编码 。
    Python 3.x默认支持编码是utf‐8,解析无障碍。
'''
#***************************************************
print()

soup1 = BeautifulSoup( "<p>中文<p>", "html.parser" )
print ( soup1.p.prettify() )
