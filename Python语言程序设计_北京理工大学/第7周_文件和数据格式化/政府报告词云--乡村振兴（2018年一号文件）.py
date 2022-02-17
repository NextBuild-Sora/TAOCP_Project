
# ------------- 政府报告词云--乡村振兴（2018年一号文件）---------- #

import jieba
import wordcloud

f = open("D:\文档\Python文件\关于实施乡村振兴战略的意见.txt", 'r', encoding='utf-8')
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(    font_path = "msyh.ttc",\
    width = 1000, height = 700, background_color = "white",\
        )

w.generate(txt)
w.to_file( "关于实施乡村振兴战略的意见（2018年一号文件）.png" )



