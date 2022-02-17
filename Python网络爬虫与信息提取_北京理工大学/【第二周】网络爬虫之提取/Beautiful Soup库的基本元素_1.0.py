
#----------------- Beautiful Soup库的基本元素_1.0 -----------------#


import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
#print ("爬取内容：" , demo)

from bs4 import BeautifulSoup
soup = BeautifulSoup( demo , "html.parser" )
aa = soup.title     #引用网页标题功能。
print ( "打印网页标题：" , aa )


#-------------------------------------------------------#
#任何存在于HTML语法中的标签都可以用soup.<tag>访问获得。
#当HTML文档中存在多个相同<tag>对应内容时，soup.<tag>返回第一个。
#-------------------------------------------------------#
#标签：
tag = soup.a    #获取a标签。
print ( "a标签：" , tag )

#标签名字：每个<tag>都有自己的名字，通过<tag>.name获取，字符串类型.
aa2 = soup.a.name   #a标签的名字。
print ( "a标签名字：" , aa2 )

aa20 = soup.a.parent.name   #a标签父类名字。
print ( "a的父类名字：" , aa20 )

aa21 = soup.a.parent.parent.name    #a标签爷爷的名字（ 父类的父 ）。
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

#标签内非属性字符串(NavigableString)：NavigableString可以跨越多个层次。
c = soup.a
c0 = c
print ("a标签树：", c0)

c1 = soup.a.string
print ("a字符串：", c1)

c2 = soup.p
print ("p标签树：", c2)

c3 = soup.p.string
print ("p字符串：" , c3)

c4 = type( soup.p.string )
print ("p字符串类型：" , c4)

#标签内字符串的注释部分（Comment）：
newsoup = BeautifulSoup( "<b><!--This is a comment--><b><p>This is not a comment</p>" , "html.parser" )
print ( "新b字符串：" , newsoup.b.string )

print ( "新b字符串类型：" , type(newsoup.b.string) )

print ( "新p字符串类型：" , type(newsoup.p.string) )


