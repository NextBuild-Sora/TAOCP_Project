#***********************************************#
#
# 5.5.2 普通爬虫程序.
# 获取网页的 HTML 代码.
#***********************************************#


import urllib.request

resp = urllib.request.urlopen("http://127.0.0.1:5000")
html = resp.read().decode()
print(html)

