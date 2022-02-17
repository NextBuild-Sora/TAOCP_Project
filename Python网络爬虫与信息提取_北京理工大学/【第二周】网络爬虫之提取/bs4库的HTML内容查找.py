
# -------- bs4库（基于）的HTML内容查找（方法） --------- #


#************************************************************************#
#                                                                        #
# **** <>.find_all(name, attrs, recursive, string, **kwargs)  ********** #
# **** 返回一个列表类型，存储查找的结果 *************************************** #
#   ∙ name : 对标签名称的检索字符串.                                          #
#   ∙ attrs: 对标签属性值的检索字符串，可标注属性检索.                            #
#   ∙ recursive: 是否对子孙全部检索，默认True.                                #
#   ∙ string: <>…</>中字符串区域的检索字符串.                                 #
#************************************************************************#



import requests

r = requests.get( "https://python123.io/ws/demo.html" )
demo = r.text
# print ( demo )

from bs4 import BeautifulSoup

soup = BeautifulSoup( demo, "html.parser" )


# ------检索（ .find_all ）a标签:
a0 = "检索a标签:"
print ( a0 , soup.find_all('a') )


# -------检索 a标签 和 b标签：
a1 = "检索a和b标签："
print ( a1 , soup.find_all( ['a', 'b'] ) )

print()


# ------遍历标签名字：
print ("标签名字：")
for tag in soup.find_all( True ):
    print ( tag.name )

print()
print ("*************************************************************")


import re   #正则表达式 库。
# ------只（仅仅）显示 b标签名字：
print("显示b标签名字：")
for tag in soup.find_all(re.compile('b')):
    print ( tag.name )


print()
print ('-------------------------------------------------------------')


# ------检索标签属性（）:
print ('检索标签course属性：')
print ( soup.find_all('p', 'course') )
print()
print ("约定查找属性，查找 id = link1 属性的值：")
print (soup.find_all( id = 'link1' ) )
print()
print ( " re查找'Link' ：", soup.find_all( id = re.compile('link') ) )



#************************************************************************************#

# ----- 扩展方法 -----                                                                 #
#                                                                                    #
#    <>.find():搜索且只返回一个结果，同.find_all()参数。                                    #
#    <>.find_parents()：在先辈节点中搜索，返回列表类型，同.find_all()参数。                    #
#    <>.find_parent()：在先辈节点中返回一个结果，同.find()参数。                              #
#    <>.find_next_siblings()：在后续平行节点中搜索，返回列表类型，同.find_all()参数。           #
#    <>.find_next_sibling()：在后续平行节点中返回一个结果，同.find()参数。                     #
#    <>.find_previous_siblings()： 在前序平行节点中搜索，返回列表类型，同.find_all()参数。       #
#    <>.find_previous_sibling()： 在前序平行节点中返回一个结果，同.find()。                    #
#    <>.find_previous_sibling()： 在前序平行节点中返回一个结果，同.find()。                    #

#**************************************************************************************#


