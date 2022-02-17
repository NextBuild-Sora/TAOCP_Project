
# --- Pandas库的数据类型操作 --- #

'''
    如何改变Series和DataFrame对象？
        增加或重排：重新索引
            删除：drop
'''

#---------------------------------------------------
#重新索引： .reindex（）能改变。
#

import pandas as pd

d1 = {'城市':['北京', '上海', '广州', '深圳', '沈阳'], 
      '环比':[101.5, 101.2, 101.3, 102.0, 100.1], 
      '同比':[120.7, 127.3, 119.4, 140.9, 101.4], 
      '定基':[121.4, 127.8, 120.0, 145.5, 101.6]}

d = pd.DataFrame( d1, index = ['c1', 'c2', 'c3', 'c4', 'c5'] )

# print (d)

d = d.reindex(index = ['c5', 'c4', 'c3', 'c2', 'c1'])
print("重排索引( 行 )： ")
print ( d )
print()

d = d.reindex ( columns = [ '定基', '环比', '同比', '城市' ] )
print("重排索引（列：专栏）： ")
print ( d )
print()

newc = d.columns.insert( 4, '新增' )
#print (newc)
newd = d.reindex( columns = newc, fill_value = "顶顶顶顶" )
print ( newd )
print()

#索引类型的使用：
nc = d.columns.delete(2)

ni = d.index.insert(5, 'c0')

# nd = d.reindex( index = ni, columns=nc, method = 'ffill' )  #运行异常
nd = d.reindex( index = ni, columns = nc ).ffill()
print ( nd )

print()

#-----------------------------------------------------
# .drop() 能够删除Series和DataFrame指定行或列索引：
a = pd.Series([9,8,7,6], index = ['a', 'b', 'c', 'd'])
print(a.drop(['b', 'c']))
print(d.drop('c5'))
print(d.drop('同比', axis = 1))
print (d)




