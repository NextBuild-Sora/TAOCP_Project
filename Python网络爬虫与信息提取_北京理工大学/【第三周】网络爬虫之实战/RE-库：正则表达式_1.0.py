
#------------ RE库 正则表达式 -------------#
# --- 1.0 版 ---


#-------------Re库的基本使用 -------

import re

# re.search(pattern, string, flags=0) 在一个字符串中搜索匹配正则表达式的第一个位置;返回match对象:
match = re.search( r'[1-9]\d{5}', 'BIt 100081' )
if match:
    print ( "re.search: " ,match.group( 0 ) ) 


# re.match(pattern, string, flags=0) 从一个字符串的开始位置起匹配正则表达式 返回match对象：
'''
# 有问题：
match = re.match( r'[1-9]\d{5}', 'BIt 100081' )
if match:
    match.group( 0 ) 
print (match.group(0))
'''

ma = re.match( r'[1-9]\d{5}', '100081 BIt' )
if ma:
    print ( 're.match: ', ma.group(0) ) 
print ( ma )


# re.findall(pattern, string, flags=0) 搜索字符串，以列表类型返回全部能匹配的子串：
ls = re.findall( r'[1-9]\d{5}', 'BIt100081 TSu100084' )
print ( 're.findall: ' , ls )


# re.split(pattern, string, maxsplit=0, flags=0) 将一个字符串按照正则表达式匹配结果进行分割 返回列表类型:
print ( 're.split: ', re.split(  r'[1-9]\d{5}', 'BIt 100081 TSU1000084' ) )
print ( 're.split: ' , re.split( r'[1-9]\d{5}', 'BIt 100081 TSU1000084', maxsplit=1 ) )


# re.finditer(pattern, string, flags=0) 搜索字符串，返回一个匹配结果的迭代类型，每个迭代 元素是match对象:
for m in re.finditer( r'[1-9]\d{5}', 'BIt100081 TSU100084' ):
    if m :
        print ( 're.finditer: ', m.group(0) )


# re.sub(pattern, repl, string, count=0, flags=0) 在一个字符串中替换所有匹配正则表达式的子串 , 返回替换后的字符串:
print ( 're.sub: ' , re.sub( r'[1-9]\d{5}', ':ziocode', 'BIT100081 TSU100084' ) )


