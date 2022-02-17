# ---------------- WordCloud库的使用 ---------------- #

# *********wordcloud应用实例2**********

import jieba
import wordcloud

# 
txt = "程序设计语言是计算机能够理解和\
    识别用户操作意图的一种交互体系，它按照\
    特定规则组织计算机指令，使计算机能够自\
    动进行各种运算处理。"

# 配置参数：宽度1000，指定字体文件的路径（默认None）,高度700.
w = wordcloud.WordCloud( width=1000,\
    font_path="msyh.ttc", height=700 )

# 加载词云文本；中文需要先分词并组成空格分割字符串。
w.generate( "".join(jieba.lcut(txt)))

# 输出词云文件
w.to_file("pywcloud.png")


