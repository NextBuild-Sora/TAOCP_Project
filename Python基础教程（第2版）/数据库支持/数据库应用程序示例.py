
# --- 数据库应用程序示例 ---


# 1、创建和填充表：

#将数据导入数据库
import sqlite3

def convert(value):
    if value.startswith('~')
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')   #连接数据库，返回连接对象。
curs = conn.cursor()    #游标对象

curs.execute( '''
CREATE TABLE food(
id    TEXT    PRIMARY KEY,
desc    TEXT,
water    FLOAT,
kcal    FLOAT )
''' )

query = 'INSERT INTO food VALUES(?, ?, ?, ?)'   #使用问号作为字段标记。

for line in open('ABBREV.txt'):     #暂时未有此文件，没有下载。
    fielda = line.split('~')
    vals = [conert(f) for f in fielda[:field_count]]
    curs.execute(query, vals)   #SQL操作

conn.commit()   #提交挂起的事务
conn.close()    #关闭连接


# 2、搜索和处理结果：

#食品数据库查询程序
import sys

conn = sqlite3.coinnect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]

print (query)

curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row ):
        print(" '%S: %s' % pair ")



