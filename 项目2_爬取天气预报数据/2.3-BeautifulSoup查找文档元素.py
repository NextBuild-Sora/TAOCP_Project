
# ---- BeautifulSoup查找文档元素 ---- #


#例2-3-1：查看文档中的<title>元素
from bs4 import BeautifulSoup

doc='''
<html><head><title>The Dormouse's story</title></head>
<body>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" 
id="link1">Elsie
</a>,
<a href="http://example.com/lacie" class="sister" 
id="link2">Lacie
</a> and
<a href="http://example.com/tillie" class="sister" 
id="link3">Tillie
</a>;
and they lived at the bottom of a well.
</p>

<p class="story">...</p>

</body>
</html>
'''

soup = BeautifulSoup(doc, "lxml")
tag=soup.find("title")
print("例2-3-1：查看文档中的<title>元素: " , type(tag), tag)

#例2-3-2：查找文档中的所有<a>元素
print("例2-3-2：查找文档中的所有<a>元素: ")
tags=soup.find_all("a")
for tag in tags:
    print(tag)

#例2-3-3：查找文档中的第一个<a>元素
tag = soup.find("a")
print("例2-3-3：查找文档中的第一个<a>元素: ")
print(tag)

#例2-3-4：查找文档中class="title"的<p>元素
tag=soup.find("p", attrs={"class":"title"})
print('例2-3-4：查找文档中class="title"的<p>元素: ')
print(tag)
tag=soup.find("p")
print("‘<p>‘元素：", tag)

#例2-3-5：查找文档中class="sister"的元素
tags=soup.find_all(name=None, attrs={"class":"sister"})
print("例2-3-5：查找文档中 class='sister' 的元素: ")
for tag in tags:
    print(tag)
tags=soup.find_all("a")     #根据打印结果，也可以是这样的方法。
tags=soup.find_all("a", attrs={"class":"sister"})   #或者是这种方法，效果一样。


print()

#  BeautifulSoup获取元素的属性值:

'''

如果一个元素已经找到，例如找到<a>元素，那么怎么样获取它的属性值呢？BeautifulSoup使用:
        tag[attrName]
来获取tag元素的名称为attrName的属性值，其中tag是一个bs4.element.Tag对象。

'''

print("**** BeautifulSoup获取元素的属性值 ****")
print()

print('#例2-3-6：查找文档中所有超级链接地址:')
soup=BeautifulSoup(doc, "lxml")
tags=soup.find_all("a")
for tag in tags:
    print(tag["href"])

print()

#BeautifulSoup获取元素包含的文本值
print("*** BeautifulSoup获取元素包含的文本值 ***")
'''
如果一个元素已经找到，例如找到<a>元素，
那么怎么样获取它包含的文本值呢？

BeautifulSoup使用: tag.text来获取tag元素包含的文本值，
其中tag是一个bs4.element.Tag对象。
'''
print("#例2-3-7：查找文档中所有<a>超级链接包含的文本值:")
for tag in tags:
    print((tag.text))

print("#例2-3-8：查找文档中所有<p>超级链接包含的文本值: ")
tags=soup.find("p")
for tag in tags:
    print(tag.text)

print()

#** BeautifulSoup高级查找 **
print("** BeautifulSoup高级查找 **")
'''
    一般find或者find_all都能满足我们的需要，如果还不能那么
可以设计一个查找函数来迚行查找。
'''

print("#例2-3-9：我们查找文档中的 href='http://example.com/lacie' 的节点元素<a> : ")
def myFilter(tag):
    print(tag.name)
    return (tag.name=="a" and tag.has_attr("href") and tag["href"]=="http://ecample.com/lacie")
soup=BeautifulSoup(doc, "lxml")
tag=soup.find_all(myFilter)
print(tag)

print("#例2-3-10：通过函数查找可以查找到一些复杂的节点元素，查找文本值以 'cie' 结尾所有<a>节点：")
def endsWith(s,t):
    if len(s) >= len(t):
        return s[len(s)-len(t):]==t
    return False

def myFilter2(tag):
    return (tag.name=="a" and endsWith(tag.text, "cie"))

soup=BeautifulSoup(doc, "lxml")
tags=soup.find_all(myFilter2)
for tag in tags:
    print(tag)
print(tags)

#------------------------------------------------------------------
print()

#例子：
def myFilter3(tag):
    #if tag.name == "p" and tag["class"]==["story"]:
    if tag.name == "p" and tag["class"]==["story"]:     #“class”是列表，要将"stoury"也改为列表，否则打印出的是空列表
        return True
soup=BeautifulSoup(doc,"html.parser")
tags=soup.find_all(myFilter3)
print("#其他例子：")
print(tags)
