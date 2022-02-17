#获取星期字符串

wStr = "星期一星期二星期三星期四星期五星期六星期日"
eKid = eval ( input ( "请输入星期数字（1-7）：" ) )
pos = ( eKid - 1 ) * 3
print ( wStr [ pos : pos + 3 ] ) 

print ()

wStr = "星期一 星期二 星期三 星期四 星期五 星期六 星期日 "  #增加一个字符
eKid = eval ( input ( " 请输入星期数字（1-7）：" ) )
pos = ( eKid - 1 ) * 4  #加一个数字
print ( wStr [ pos : pos + 4 ] )  #加一个数字

print ()
