# 遍历循环

for i in range (8): 	# 计数循环
	print (i)

for a in range(5):
	print ('dddddddd',a)

for i in range (1,6): 	#计数循环（特定次）：1到5。
	print (i)

for i in range (1,6,2): 	#计数循环（特定次）：1到5,2个步长。
	print ('aaaaa',i)

for a in range (3,9):
	print ('aa',a)

for a1 in range (3,9,2):
	print ('nnn',a1)

for c in 'python123456': 	# 字符串循环
	print (c, end = ',' )

	
for it in [1,3,'bb',2356,0]: 	# 列表循环
	print (it , end ="~")

# 还有文件循环（现在暂时无法实现）


# 无限循环：由条件控制的循环运行方式。
# while：反复执行语句块，直到条件不满足时结束。

啊 = 10
while 啊 > 0:
	啊 = 啊 - 1
	print (啊)

