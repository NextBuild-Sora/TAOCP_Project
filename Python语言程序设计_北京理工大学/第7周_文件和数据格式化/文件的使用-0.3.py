
# ----------------------------文本的全文本操作：遍历全文本---------------------------- #


# 方法一：
# 一次读入，统一处理。
fname = input( "输入要打开的文件名称：" )
fo = open( fname, 'r' )

txt = fo.read( )     # 对全文txt进行处理

print ("方法一：", txt )

fo.close( )


#----------------------------#


# 方法二：
# 按数量读入，逐步处理。
fname = input( "输入要打开的文件名称：" )
fo = open( fname, 'r' )

txt = fo.read( 2 )    # 数量

while txt != "":
    # 对txt进行处理。
    txt = fo.read( 2 )
    
print ( "方法二：", txt )

fo.close( )
