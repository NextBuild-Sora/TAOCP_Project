
import urllib.request   #引入urllib.request程序包, 作用是访问网站。

url = "http://127.0.0.1:5000"

resp = urllib.request.urlopen(url)  #这条语句的作用是打开url网址的网址,urllib.request是urllib中的一个子程序包，urlopen是打开网站的函数。
data = resp.read()  #这个网站打开后就如同打开文件一样，要使用read函数读取网站的内容，读出的二进制数据.
html = data.decode()    #这条语句的作用是把二进制数据html转为字符串, 默认时decode()是使用utf-8编码.

print(html)     #显示网站的网页内容，由此可见传递过来的就是index.htm的网页数据.

