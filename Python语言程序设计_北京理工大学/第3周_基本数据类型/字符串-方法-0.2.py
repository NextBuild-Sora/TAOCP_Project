
# 字符串处理方法（部分）
# 一些以方法形式提供的字符串处理功能

##########################################################################
##                                                                       ##
# -------------- <a>.<b> 风格；<a>是字符串.<b>是方法（函数） ------------- ##
##                                                                       ##
# ----- str.lower() 小; str.upper() 大 ；返回字符串的副本，全部 小/大 写。------ ##
# ----- split()  分离；   返回一个列表。 -------------------------------------- ##
# ----- count('a') 计数；    返回子串a(某个字符)出现的次数。 ------------------- ##
# ----- replace(a,b) 替代；   返回副本，a字之差u呢 替换为比。 ------------------ ##
# ----- center(10[,b]) 居中； 字符串根据宽度 10 居中，b可选。 ------------------ ##
# ----- strip( a ) 脱去；    从字符串中去掉其 啊 左侧和右侧中列出的字符.  ------- ##
# ----- join( a ) 结合；  在 a 变量 除最后元素外每个元素后增加一个str。 --------- ##
##                                                                       ##
###########################################################################

print ()
a = str.lower ("aDggFVjn")
a3 = 'bBBBbb'.lower()
print (a)
print (a3)
print ()

a1 = str.upper('adfFDDFDfjF')
a4= 'anMMjjkllk'.upper()
print (a1)
print (a4)
print ()

b = str.split('asdfgh')
print (b)
b1 = 'bnmkjh'.split()
print (b1)
print ()

# c = str.count('lkjhgg')  错误用法
c1 = 'mmmmmmmmm'.count ('m')
print (c1)
# print (c)
print ()

# e = str.replace('aaa')  错误用法
e1 = 'python' .replace('p','P')
# print (e)
print (e1)
print ()

# f = str.center(10,"=")
f1 = 'qqqq'.center(15,"-")
# print (f)
print (f1)
print ()

d = "= mmm =j".strip(' =j')
print (d)
print ()

g = "dfg,".join('1234')
print (g)
print()

