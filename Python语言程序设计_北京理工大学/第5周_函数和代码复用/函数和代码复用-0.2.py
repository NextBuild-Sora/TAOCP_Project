# 局部变量和全局变量
# 局部变量是函数内部的占位符，与全局变量可能重名但不同
# 函数运算结束后，局部变量被释放
# 可以使用global保留字在函数内部使用全局变量

# 规则1: 局部变量和全局变量是不同变量

n , s = 10 , 100    # 全局变量
def fa(n):
    s = 1   # 局部变量
    for i in range (1,n+1):
        s *= i
    return s    # 此处 s 是局部变量。
print (fa(n),s)     # 这里的 s 是全局变量。

print ()

n1 , s1 = 20 , 200
def fa1():
    global s1   # 使用global保留字声明，此处s1是全局变量s1.
    for i in range(1,n+1):
        s1 *= i
    return s1    # 此处s1指全局变量s1.
print (fa1(),s1)   # 此处全局变量s1被函数修改。

print ()

# 规则2: 局部变量为组合数据类型且未创建，等同于全局变量.
ls = ['F','f']  # 通过使用[]真实创建了一个全局变量列表ls.
def ru(a):
    ls .append(a)   # 此处 ls 是列表类型，未真实创建，则等同于全局变量。
    return
ru('aC')    # 全局变量 ls 被修改。
print (ls)

print()

ls1 = ['aaa', 'bbb','ccc']
def ru1(a):
    ls1 = []    # 此处ls1是列表类型，真实创建，ls是局部变量。
    ls1.append(a)
    return
ru1('mz=zm')    # 局部变量 ls1 被修改。
print(ls1)

print()

