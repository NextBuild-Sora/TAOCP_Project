

# ---- BeautifulSoup遍历文档元素 ---- #


from bs4 import BeautifulSoup

doc='''

<html><head><title>The Dormouse's story</title></head>
<body>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">
Once upon a time there were three little sisters; and their names 
were
<a href="http://example.com/elsie" class="sister" 
id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" 
id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" 
id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>

<p class="story">...</p>

</body>
</html>

'''


#获取元素节点的父节点
''' BeautifulSoup通过：tag.parent 获取tag节点的父节点. '''

#例2-4-1：找出文档中<p class="title"><b>The Dormouse's story</b></p>的<b>元素节点的所有父节点的名称。
soup=BeautifulSoup(doc, "lxml")
print("<b>元素节点的所有父节点的名称。")
print(soup.name)
tag=soup.find("b")
while tag:
    print(tag.name)
    tag=tag.parent
    
print()

print("*** 获取元素节点的直接子元素节点 ***")
#tag.children 获取tag节点的所有直接子节点，包括element、text等类型的节点。

#例2-4-2：获取<p>元素的所有直接子元素节点
tag=soup.find("p")
print("<p>元素的所有直接子元素节点: ")
for x in tag.children:
    print(x,'\n')

print("*** 获取元素节点的所有子孙元素节点 ***")
#tag. desendants获取tag节点的所有子孙节点元素

#例2-4-3：获取<p>元素的所有子孙元素节点
tag=soup.find("p")
for x in tag.descendants:
    print( x)

print()
print("*** 获取元素节点的兄弟节点 ***")
# tag.next_sibling ：获取下一个；是tag的临近的下一个兄弟节点。
# tag.previous_sibling ：前一个兄弟节点；是tag的临近的前一个兄弟节点。

doc1=''' 
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The <i>Dormouse's</i> story</b> Once upon a 
time ...</p>
</body>
</html>
 '''

#例2-4-4：查找前后兄弟节点
soup=BeautifulSoup(doc1, "lxml")
tag=soup.find("b")
print("前一个：", tag.previous_sibling)
print("下一个：", tag.next_sibling)
print()
tag=soup.find("i")
print("前一个：", tag.previonus_sibling)
print("下一个：", tag.next_sibling)
print()







