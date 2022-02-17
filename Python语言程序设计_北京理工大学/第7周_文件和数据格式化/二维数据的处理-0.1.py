
# *************** 二维数据的处理 *************** #

# 读入处理：从CSV格式的文件中读入数据
fo = open( "D:\文档\Python文件\二维数据的处理-0.3.csv", encoding='UTF-8' )

ls = [ ]

for line in fo:
    line = line.replace( "\n", ' ' )
    ls.append( line.split( "," ) )
    
# print( "读入处理：" , fo)

fo.close( )


#****************************************************************#
'''
# 写入处理：将数据写入CSV格式的文件
ls1 = [ [], [], [] ]     # 二维列表

f = open("D\文档\Python文件\二维数据的处理-0.4.csv", encoding = 'UTF-8' , 'w' )

for item in ls1:
    f.write( ','.join(item) + '\n' )

f.close()
'''
#****************************************************************#

