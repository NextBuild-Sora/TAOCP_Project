
#-------------- bs4库的HTML内容遍历方法 ———————————————#

import requests
r = requests.get( "http://python123.io/ws/demo.html" )
demo = r.text
# print (demo)

from bs4 import BeautifulSoup

# 标签树的下行遍历：
#---------------------------------------------------------
'''
    .contents ：说明 子节点的列表，将<tag>所有儿子节点存入列表。。
    .children ：子节点的迭代类型，与.contents类似，用于循环遍历儿子节点。
    .descendants : 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历。
'''
#---------------------------------------------------------
soup = BeautifulSoup( demo, "html.parser" )
print ( "头部信息：", soup.head )

print ( "head字节点的列表：", soup.head.contents )

print ( "body节点的列表：", soup.body.contents )

print ( "body节点的数量：", len(soup.body.contents) )

print ( "位于列1的body节点：", soup.body.contents[1] )
#print ( "body节点列1:", a )

# 遍历儿子节点:
for chile in soup.body.children:
    print ()
    print ( "儿子节点：", chile )

# 遍历子孙节点：
for child in soup.body.descendants:
    print ()
    print ( "子孙节点：", child )

