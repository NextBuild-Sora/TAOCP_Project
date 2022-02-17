# ---------------- WordCloud库的使用 ---------------- #

# *********wordcloud库常规方法**********


import wordcloud
c = wordcloud.WordCloud()           # -步骤1、配置对象参数：以WordCloud对象为基础，配置参数、加载文本、输出文件。
c.generate("wordcloud by Python")   # -步骤2、加载词云文本：向WordCloud对象c中加载文本。
c.to_file("pywordcloud.png")        # -步骤3、输出词云文件：将词云输出为图像文件， .png或.jpg格式。

# print(c)
