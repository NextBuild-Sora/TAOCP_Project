#温度转换

T123 = input ("输入带有符号的温度值：")
if T123 [-1] in [ 'F' , 'f' ]:
    C = (eval ( T123 [ 0:-1 ] ) - 32 ) /1.8
    print ('转换后的温度是 {:.2f} c' .format ( C ) )

    '''print ('转换后的温度是{:.2f}C' ).format ( C )) 
                                    # .format前面多了个右括号，导致出现异常'''
        
elif T123 [ -1 ] in [ 'C' , 'c' ]:
    F = 1.8 * eval ( T123 [ 0 : -1 ] ) + 32
    print ( "转换后的温度是 {:.2f} F" .format ( F ) )
        
else :
    print("输入格式错误！")

