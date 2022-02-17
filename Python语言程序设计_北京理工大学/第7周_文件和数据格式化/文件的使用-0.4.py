
# ----------------------------文本的逐行操作: 逐行遍历文件---------------------------- #


# 方法一：
# 一行读入，分行处理。
fname = input( "请输入要打开的文件名称：" )
fo = open ( fname, "r" )

for line in fo.readlines():
    print( "逐行操作_方法一：", line)

fo.close()


#----------------------------#


# 方法二：
# 分行读入，逐行处理。
fn = input( "文件名称：" )
f1 = open( fn, "r" )

for lien in f1:
    print( "方法二：", line)

f1.close()
