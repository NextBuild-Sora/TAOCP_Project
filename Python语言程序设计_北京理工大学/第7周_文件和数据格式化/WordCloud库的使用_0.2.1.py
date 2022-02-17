# ---------------- WordCloud库的使用 ---------------- #

# *********wordcloud应用实例**********


import wordcloud

txt = "Hello, world!\
        Welcome to Python."

w = wordcloud.WordCloud( \
    background_color = "white" )

w.generate(txt)

w.to_file( "Hello,World!.png" )


