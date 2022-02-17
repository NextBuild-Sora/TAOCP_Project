
#-------------- bs4库的HTML内容遍历方法 ———————————————#

import requests
r = requests.get( "http://python123.io/ws/demo.html" )
demo = r.text
# print (demo)

from bs4 import BeautifulSoup

# ------------- 标签树的平行遍历：
#----------------------------------------------------
'''
    --- .next_sibling：返回按照HTML文本顺序的下一个平行节点标签。
    --- .previous_sibling ：返回按照HTML文本顺序的上一个平行节点标签。
    --- .next_siblings：迭代类型，返回按照HTML文本顺序的后续所有平行节点标签。
    --- .previous_siblings ：迭代类型，返回按照HTML文本顺序的前续所有平行节点标签。
'''
#----------------------------------------------------

soup = BeautifulSoup( demo, "html.parser" )

print ( "下一个平行节点标签树：" , soup.a.next_sibling )

print ( "平行节点标签树：" , soup.a.next_sibling.next_sibling )

print ( "‘soup.a’的上一个平行节点标签树：", soup.a.previous_sibling )

print ( "标签：" , soup.a.previous_sibling.previous_sibling )

print ( "‘soup.a’ 父标签树：" , soup.a.parent )

# 遍历后续节点：
print ( "遍历后续节点：" )
for sibling in soup.a.next_sibling:
    print ( sibling )

# 遍历前续节点：
print ( "遍历前续节点：" )
for sibling in soup.a.previous_sibling:
    print ( sibling )