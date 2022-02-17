
######################################################

# ------------ “基本统计值”问题分析 ------------------#
'''

- 需求：给出一组数，对它们有个概要理解。


- 该怎么做呢？
    总个数、求和、平均值、方差、中位数…

    - 总个数：len()    
    - 求和：for … in
    - 平均值：求和/总个数

    - 方差：
    各数据与平均数差的平方和的平均数。

    - 中位数：
    排序，然后… 奇数找中间1个，偶数找中间2个取平均

'''

######################################################

# 1、获取多数据输入。 2、通过函数分隔功能。

def getNum( ):   # 获取用户不定长度的输入。
    nums = [ ]
    iNumStr = input( "请输入数字（回车退出）：" )
    while iNumStr != "" :
        nums.append(eval ( iNumStr ) )
        iNumStr = input( "请输入数字（回车退出）：" )
    return nums

def mean( numbers ):  # 计算平均值。
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len( numbers ) 

def dev( numbers, mean ):     # 计算中位数。
    sdev = 0.0
    for num in numbers:
        sdev = sdev + ( num - mean ) ** 2
    return pow(sdev / ( len( numbers ) -1 ), 0.5 )

def median(numbers):
    sorted(numbers)     # sorted函数：排序。
    size = len(numbers)
    if size % 2 == 0:
        med = ( numbers[ size // 2-1 ] + numbers [ size // 2 ] ) / 2
    else:
        med = numbers [size // 2]
    return med


n = getNum( )
m = mean ( n )
print ( "平均值：{}, 方差:{:.2}, 中位数：{}。" .format( m, dev( n , m ), median ( n ) ) )
