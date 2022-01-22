

# ---- BeautifulSoup使用CSS语法查找元素 ---- #

'''

    *** 2.5.1 使用 CSS 语法 ***
    BeautifulSoup 除了可以用 find 与 find_all 函数查找 HTML 文档树的节点元素外，还可
以采用 CSS 类似的语法来查询，规则是：
    tag.select(css)
    其中 tag 是一个 bs4.element.Tag 对象，即 HTML 中的一个 element 节点元素，select 是
它的查找方法，css 是类似 css 语法的一个字符串，一般结构如下：
    [tagName][attName[=value]]
    其中[...]部分是可选的；
    tagName 是元素名称，如果没有指定就是所有元素；
    attName=value 是属性名称，value 是它对应的值，可以不指定属性，在指定了属性后也
可以不指定值；
    tag.select(css)返回一个 bs4.element.Tag 的列表，哪怕只有一个元素也是一个列表；

'''


from bs4 import BeautifulSoup

doc='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
</body>
</html>
'''


#例 2-5-1：soup.select("a") 查找文档中所有<a>元素节点；
'''
soup=BeautifulSoup(doc, "lxml")
soup.select("p a")      #查找文档中所有<p>节点下的所有<a>元素节点；
soup.select("p[class='story'] a")   #查找文档中所有属性 class="story"的<p>节点下的所有<a>元素节点；
soup.select("p[class] a")   #查找文档中所有具有 class 属性的<p>节点下的所有<a>元素节点；
soup.select("a[id='link1']")    #查找属性 id="link1"的<a>节点；
soup.select("body head title")  #查找<body>下面<head>下面的<title>节点；
soup.select("body [class] ")    #查找<body>下面所有具有 class 属性的节点；
soup.select("body [class] a")   #查找<body>下面所有具有 class 属性的节点下面的<a>节点；
'''

#例 2-5-2： 查找 HTML 文档中所有<p>下面的<a>的链接：
soup=BeautifulSoup(doc, "lxml")
tags=soup.select("p[class='story'] a")

print(" 所有<p>下面的<a>的链接: ")
for tag in tags:
    print(tag["href"])

#也可以通过这3种方法，得到一样的结果：
tags=soup.select("p a")
tags=soup.select("a")
tags=soup.select("p[class] a")
print()

#例 2-5-3：查找子孙节点：
#节点元素之间用空格分开，就是查找子孙节点.
print("子孙节点：")
doc0="<div><p>A</p><span><p>B</p></span></div><div><p>C</p></div>"

soup0=BeautifulSoup(doc0, "lxml")
tags=soup0.select("div p")
for tag in tags:
    print(tag)

print()
#例 2-5-4：查找直接子节点:
docs ="<div><p>A</p><span><p>B</p></span></div><div><p>C</p></div>"

soup=BeautifulSoup(docs, "lxml")
tags=soup.select("div > p")     #用 > (注意 > 的前后至少包含一个空格)，表示查找直接子节点

print("子节点：")
for tag in tags:
    print(tag)

print()
#例 2-5-5：查找兄弟节点：

doc11="<body>demo<div>A</div><b>X</b><p>B</p><span><p>C</p></span><p>D</p></div></body>"
soup11=BeautifulSoup(doc11, "lxml")
print("美丽化：", soup11.prettify())

print("*************")
print("兄弟节点：")
tags=soup11.select("div ~ p")    #用" ~ "连接两个节点表示查找前一个节点后面的所有同级别的兄弟节点（注意~号前后至少有一个空格）。
for tag in tags:
    print(tag)
print()

print("兄弟节点2：")
tags=soup11.select("div + p")    #用" + "连接两个节点表示查找前一个节点后面的第一个同级别的兄弟节点（注意+号前后至少有一个空格）。
for tag in tags:
    print(tag)  #下一个兄弟节点是<b>X</b>，不是<p>节点，因此没有找到.

print()



