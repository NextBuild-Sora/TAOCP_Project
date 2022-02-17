
# Requests库的安装小测

import requests
r = requests.get( "https://www.baidu.com" )
print( r.status_code )

a = r.text
print( a )



