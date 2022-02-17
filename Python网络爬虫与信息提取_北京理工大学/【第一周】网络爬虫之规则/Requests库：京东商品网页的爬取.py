
# ---------------- Requests库:京东商品网页的爬取 ---------------- #

import requests

url = "https://item.jd.com/100014565820.html"

try:
    r = requests.get( url )
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print ( "京东商品：", r.text[:1000])
except:
    print ( "爬取失败" )


