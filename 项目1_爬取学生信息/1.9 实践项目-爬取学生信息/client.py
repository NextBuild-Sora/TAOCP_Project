
# 客户端程序

'''
    客户端的爬虫程序，它从这个网页上爬行学生的这
些信息，存储到数据库中。学生数据库可以使用Sqlite数据库
students.db。

    0-客户端程序访问http://127.0.0.1:5000/的网址，从中下载其HTML网页.
    1-要从这个HTML网页爬取数据，只要分解出第一行:<tr></tr>
    2-再次分解这一行的<td>...</td>数据.
    3-接下来再次分解出下一行<tr>...</tr>.
    4-再次分解这一行的<td>...</td>数据.把这一行的数据写入对应的数据库即可。
    5-要分解出<tr>...</tr>只要使用r"<tr>"与r"</tr>"的正则表达式即可.

'''

import urllib.request
import re

try:
    resp = urllib.request.urlopen("http://127.0.0.1:5000")
    data = resp.read()
    html = data.decode()
    m = re.search(r"<tr>", html)
    n = re.search(r"</tr>", html)
    while m!=None and n!=None:
        row = html[m.end() : n.start()]
        a = re.search(r"<td>", row)
        b = re.search(r"</td>", row)
        while a!=None and b!=None:
            row = html[m.end() : n.start()]
            a = re.search(r"<td>", row)
            b = re.search(r"</td>", row)
            while a!=None and b!=None:
                s = row[a.end() : b.start()]
                print(s, end='')
                row = row[b.end(): ]
                a = re.search(r"<td>", row)
                b = re.search(r"</td>", row)
            print()
            html = html[n.end(): ]
            m = re.search(r"<tr>", html)
            n = re.search(r"</tr>", html)
except Exception as e:
    print("捕捉到错误信息：", e)


