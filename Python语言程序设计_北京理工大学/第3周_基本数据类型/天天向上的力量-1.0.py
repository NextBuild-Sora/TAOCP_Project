
#5‰和1%的力量


'''
     - 一年365天，每天进步5‰或1%，累计进步多少呢？

                                 1.005 ；1.01
                                 
     - 一年365天，每天退步5‰或1%，累计剩下多少呢？

                                 0.995 ； 0.99
                                 
'''


dayfactor = 0.005
dayup = pow ( 1 + dayfactor , 365 )
daydown = pow ( 1 - dayfactor , 365 )
print ( " 进步5‰  向上：{:.2f}  \n 退步5‰  向下：{:.2f} " .format ( dayup , daydown ) )

print ()


力量1 = 0.01
进步1 = pow (1 + 力量1 , 365 )
退步1 = pow ( 1 - 力量1 , 365 )
print ( " 进步1% ：{:.2f}, \n 退步1%：{:.2f} " .format ( 进步1 ,退步1 ) )

print ( )

