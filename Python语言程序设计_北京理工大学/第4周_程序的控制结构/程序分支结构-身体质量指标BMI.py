# ------------------------------------------------------------------- #
# ------- 身体质量指数BMI：BMI=体重（kg）/身高（m） ------------- #

# -- 问题：输入给定体重和身高值；输出BMI指标分类信息(国际和国内) -- #

# ---- 难点：同时输出国际和国内对应的分类。
# ---- 思路1：分别计算并给出。
# ---- 思路2：混合计算并给出。
# ------------------------------------------------------------------- #


# 思路1
print ( ' ----- 分别计算 ：----- ' )
print ( )

he , we = eval(input("输入身高(米)和体重(公斤)【逗号隔开】：" ))
bm = we / pow(he,2)

print ('BIM数值为：{:.2f}' .format(bm))

# 国际：
who = ''
if bm < 18.5:
    who = '偏瘦'
elif 18.5 <= bm < 25:
    who = '正常'
elif 25 <= bm <30:
    who = '偏胖'
else:
    who = '肥胖'
print ('BMI（国际）指标：{0} ！' .format(who))


# 国内：
na = ''
if bm < 18.5:
    na = '偏瘦'
elif 18.5 <= bm < 24:
    na = '正常'
elif 24 <= bm <28:
    na = '偏胖'
else:
    na = '肥胖'
print ('BMI（国内）指标：{0} ！' .format(na))

print ()


# 思路2

print ( ' ----- 混合计算 ：----- ' )
print ()

he,we = eval(input ( " 输入身高 m ，体重 kg [逗号隔开]：" ))
bm = we / pow( he , 2 )
print ( " BMI：{:.2f} " .format( bm )  )
wh , na = ' ' , ' '
if bm < 18.5:
    wh , na = '偏瘦' , '偏瘦'
elif 18.5 <= bm < 24:
    wh , na = '正常' , '正常'
elif 24 <= bm < 25:
    wh , na = '正常' , '偏胖'
elif 25 <= bm < 28 :
    wh , na = '偏胖' , '偏胖'
elif 28 <= bm <30 :
    wh , na = '偏胖' , '肥胖'
else:
    wh , na = '肥胖' , '肥胖'
print ( " BMI国际指标：{0} ，国内指标：{1}  " .format( wh , na ) )

print ()


