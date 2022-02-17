# 文本词频统计-哈姆雷特-英文版

# 对独立的文本进行归一化处理：
def getText():
    txt = open( 'D:\文档\Python文件\hamlet.txt' , 'r' ) .read()
    txt = txt.lower()   # lower：小写。表达将的是：txt 进行小写转换。
    # 归一化：
    for ch in ' !"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~ ': 
        txt = txt.replace( ch , " " )   # 替换特殊符号为空格。
        return txt

hamletTxt = getText( ) # 归一化
words = hamletTxt.split()   # 列表形式；split函数：将字符串的信息用空格分隔，以列表的形式返回给变量。
counts = {}     # 表达单词跟出现频率的对应关系（映射类型）。

# 遍历词频出现次数：
for word in words:  
    counts[word] = counts.get( word , 0 ) + 1   # 获取单词出现的次数。
    
items = list( counts.items() )  # 对词频出现次数进行排序。

items.sort( key = lambda x : x[1], reverse=True )   # 通过排序获得当前最高的单词出现次数。

for i in range(10):     # 对前10位单词出现次数的元素以及它的次数进行打印输出。
    word, count = items[i]
    print( "{0:<10}{1:>5}"  .format( word,count )  )

