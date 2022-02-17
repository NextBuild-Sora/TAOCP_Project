
#----------------- Beautiful Soup库的基本元素 -----------------#

#*******************************************************************************************#
#    Beautiful Soup库：是解析、遍历、维护“标签树”的功能库.
#   Beautiful Soup库，也叫：beautifulsoup4 或 bs4,约定引用方式如下，即主要是用BeautifulSoup类:
#       from bs4 import BeautifulSoup
#       import bs4
#*******************************************************************************************#
#   from bs4 import BeautifulSoup
#    soup = BeautifulSoup("<html>data<html>" , "html.parser" )
#   soup2 = BeautifulSoup(open("D://demo.html") , "html.parser" )
#            BeautifulSoup对应一个HTML/XML文档的全部内容.
#*******************************************************************************************#
#   基本元素: <p class=“title”> … </p>                                          *************#
#   ----------------------------------------------------------------------------------------#
#   --基本元素--              --说明--                                            ************#
#    Tag :                标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾.        ************#
#    Name :               标签的名字，<p>…</p>的名字是'p'，格式：<tag>.name.         ************#
#    Attributes :         标签的属性，字典形式组织，格式：<tag>.attrs.                ************#
#    NavigableString :    标签内非属性字符串，<>…</>中字符串，格式：<tag>.string.      ************#
#     Comment :            标签内字符串的注释部分，一种特殊的Comment类型.              *************#
#*******************************************************************************************#



import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
print ("爬取内容：" , demo)

from bs4 import BeautifulSoup
soup = BeautifulSoup( demo , "html.parser" )
aa = soup.title     #引用网页标题功能
print ( "打印网页标题：" , aa )

#任何存在于HTML语法中的标签都可以用soup.<tag>访问获得
#当HTML文档中存在多个相同<tag>对应内容时，soup.<tag>返回第一个
#标签：
tag = soup.a    #获取a标签
print ( "a标签：" , tag )

#标签名字：每个<tag>都有自己的名字，通过<tag>.name获取，字符串类型.
aa2 = soup.a.name   #a标签的名字
print ( "a标签名字：" , aa2 )

aa20 = soup.a.parent.name   #a标签父类名字
print ( "a的父类名字：" , aa20 )

aa21 = soup.a.parent.parent.name    #a标签爷爷的名字（ 父类的父 ）
print ( "a爷爷名字：" , aa21 )

#标签的属性：一个<tag>可以有0或多个属性，字典类型。
tag1 = soup.a
bb1 = tag1.attrs     #标签的属性
print ( "a标签的属性" , bb1 )

bb10 = tag1.attrs['class']
print ( "标签属性的Class：" , bb10 )

bb11 = tag1.attrs['href']
print ( "标签的Href：" , bb11 )

print ( "类型属性：" , type(tag1.attrs) )
print ( "类型：" , type(tag1) )



