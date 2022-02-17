
# ----------------------- os库的使用_0.3 ---------------------------- #


# ----- 环境参数：获取或改变系统环境信息---------

import os

# a = os.chdir("D:")    #修改当前程序操作路径。
# print(a)
print()

b = os.getcwd ()     #获取（返回）程序的当前路径。
print ( "程序的当前路径：" , b )

print()

c = os.getlogin()   #获取当前系统登录用户名称。
print ( "当前系统用户名：" , c )

print()

e = os.cpu_count()  #获得当前系统的CPU数量。
print ( 'CPU数量：' , e )

print()

d = os.urandom(10)  #获得10个字节长度的随机字符串，通常用于加解密运算。
print ( "随机字符串：" , d )

print()

