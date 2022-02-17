# 汉诺塔

'''

- 函数 + 分支结构
- 递归链条
- 递归基例

'''


count = 0
def hanoi ( n, src, dst, mid ):
    global count
    if n == 1:
        print ( "{} : {} -> {}" .format( 1, src, dst ) )
        count += 1
    else:
        hanoi ( n-1, src, mid, dst )
        print ("{} : {} -> {}" .format( n, src, dst ) )
        count += 1
        hanoi ( n-1, mid, dst, src )
hanoi ( 3, "A", "C", "B" )
print (count)


