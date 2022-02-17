# 循环控制保留字
# break：跳出并结束当前整个循环，执行循环后的语句。
# continue：结束当次循环，继续执行后续次数循环。
# 这两个可以与for和while循环 搭配使用。

for c in 'python':
    if c == 't':    # 变量c循环到‘t’时。
        continue    # 结束当次循环，继续后续次数循环。
    print (c,end='~')

print ()

for c in "python":
    if c == 't':    # 循环到变量c（'t'）时。
        break   # 跳出当前（'t'之后的）整个循环，执行循环后的语句。
    print (c,end='*')   # 循环后的语句。

print ()

s = 'python12'
while s != '':
    for c in s:
        print (c,end='~')
    s = s[:-1]

print ()

s = 'python38'
while s != '':
    for c in s:
        if c == 't':
            break   # 仅跳出当前最内层循环。
        print (c,end='*')
    s = s[:-1]

print()

# 循环与else
# 当循环没有被“跳出”语句退出时，执行else语句块。
# 与异常处理中else用法相似。

for c in 'pyton':
    if c == 't':
        continue
    print (c,end='/')
else:
    print ('正常退出')

print()

for c in 'python123':
    if c == 't':
        break
    print (c,end='~')
else :
    print ('正常退出！！！')

print()

