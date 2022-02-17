

# ---------------- Beautiful Soup库的安装小测 ---------------- #

import requests

r = requests.get("http://python123.io/ws/demo.html")
#a = r.text
#print ( "看一下结果：", a )
demo = r.text

from bs4 import BeautifulSoup    
soup = BeautifulSoup(demo , 'html.parser')

print(soup.prettify())



