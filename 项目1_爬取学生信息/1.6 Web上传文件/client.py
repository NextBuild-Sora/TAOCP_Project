

import urllib.request

url = "http://127.0.0.1:5000"
fileName = "《Python web程序开发技术》.pdf"
try:
    fobj = open(fileName, 'rb')
    data = fobj.read()
    fobj.close()
    headers = {'content-type': 'application/octet-stream'}
    url = url + '?fileName=' + urllib.parse.quote(fileName)
    req = urllib.request.Request(url, data, headers)
    resp = urllib.request.urlopen(req)
    msg = resp.read().decode()
    print(msg)
except Exception as e:
    print(e)


