
#-------------- bs4库的HTML内容遍历方法 ———————————————#

import requests
r = requests.get( "http://python123.io/ws/demo.html" )
demo = r.text
# print (demo)

from bs4 import BeautifulSoup

# ------------- 标签树的上行遍历：
#----------------------------------------------------
'''
    .parent ：节点的父亲标签。
    .parents ：节点先辈标签的迭代类型，用于循环遍历先辈节点。
'''
#----------------------------------------------------

soup = BeautifulSoup( demo, "html.parser" )

print ( "title父标签：" , soup.title.parent )

print ( "HTML父亲标签：", soup.html.parent )

print ( "parent父标签：" , soup.parent )


# 打印 soup.a 先辈标签名字：
for parent in soup.a.parents:
    if parent is None:
        print( parent )
    else:
        print ( parent.name )

