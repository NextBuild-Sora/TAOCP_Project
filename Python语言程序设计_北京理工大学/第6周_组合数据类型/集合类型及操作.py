# 集合类型及操作
'''
集合是多个元素的无序组合
- 集合类型与数学中的集合概念一致 
- 集合元素之间无序，每个元素唯一，不存在相同元素 
- 集合元素不可更改，不能是可变数据类型。 为什么？
- 集合用大括号 {} 表示，元素间用逗号分隔 
- 建立集合类型
- 建立空集合类型，必须使用set()
'''

'''
s | t :并，返回一个新集合（所有的元素）。
s - t :差，返回一个（集合s，不在t的元素）新集合。
s & t :交，返回一个新集合，包括同时在集合s和t中的元素。
s ^ t :补，返回一个新集合，包括集合s和t中的非相同元素。
s <= t 或 s < t ：判断s和t的子集关系，返回True/False.
s >= t 或 s > t ：判断s和t的包含关系，返回返回True/False.

s |=t :并，更新集合s，包括在集合s和t中的所有元素。
s -= t :差，更新集合s，包括在集合s但不在t的元素
s &= t :交，更新集合s，包括同时在集合s和t中的元素。
s ^= t :补，更新集合s，包括集合s和t中的非相同元素。

集合处理方法：
a.add(x):如果x不在集合a中，将x增加到a。
a.discard(x):移除a中元素x，不在集合中也不报错。。。
a.remove(x):移除a中元素x，不在集合中会产生keyError异常。。。
a.clear():移除a中所有元素。
a.pop():随机返回一个元素，更新a，若为空产生keyError异常。
呵.copy():返回集合 呵 的一个副本。
len(a):返回集合a的元素个数。
z in b:判断z中元素b是否存在。。。
z not in s :判断z中元素s，是否不存在。
set(a):将其他类型变量a转变为集合类型。

'''


a = {"p","y",123}
for o in a:
    print ("判断元素：", o, end=' ')

print()

try:
    while True:
        print (a.pop(), end="~")
except:
    pass 
    print()
    print("随机返回元素；退出。")

print ()

'p' in {'p','y',12}     # 包含关系比较：是否存在。
if 'p' in {'p','y',12}: 
    print (" 包含：True ")
else:
    print(" 不包含：False ")

if {"p","y"} >= {"p","y",123}:
    print ("True")
else:
    print('False')

print()

ls=["p","p","y","y",123]
s = set(ls)     # 利用了集合无重复元素的特点。
print("转换集合类型：",s)

lt = list(ls)   # 还可以将集合转换为列表。
print ("转换列表：",lt)
