# -*- Pandas库的数据排序 -*-


import pandas as pd
import numpy as np


#******************************************************
"""
        .sort_index()方法在指定 轴 上根据 索引 进行排序，默认升序 
            .sort_index( axis=0, ascending=True )
"""
#-------------------------------------

b = pd.DataFrame( np.arange(20).reshape(4,5), index = ['c', 'a', 'd', 'b'] )
print( "b数列： " , '\n', b )

print()

print ( "索引排序： " '\n', 
       b.sort_index() )
print()

print ( "降序： " '\n' , 
       b.sort_index(ascending = False) )
print()

c = b.sort_index( axis = 1, ascending = False )
print( "c数列 轴1降序： " '\n', 
      c )

c = c.sort_index()
print( 'c数列 索引排序： ' "\n",
      c )

print()
#*****************************************************


'''    
    .sort_values()方法在指定轴上根据 数值 进行排序，默认升序
    
    Series.sort_values( axis=0, ascending=True ) 
    DataFrame.sort_values( by, axis=0, ascending=True ) 
    by : axis轴上的某个索引或索引列表

'''
#-----------------------------------------

print( "--数值排序--： ")

# .sort_values(by, axis = 0 , ascending = True ): 
c = b.sort_values( 3, ascending = False )
print( "轴2降序： "  '\n' ,
      c )
print()

c = c.sort_values( 'a', axis = 1, ascending = False  )
print( "c数列的a索引-轴1降序： "  '\n' 
      , c )
print()

# NaN统一放到排序末尾： 
a = pd.DataFrame( np.arange(12).reshape(3,4), index= ['a', 'b', 'c'] )
print( "a数列： " '\n', a)
print()

print( "b数列： " '\n', b )
print()

c = a + b 
print( "a+b运算： " '\n' , c )

print()

c1 = c.sort_values( 1, ascending = False )  #数值轴2进行降序
c2 = c.sort_values( 2, ascending = True )   #数值轴2进行升序
print( c1,
      '\n',
      c2)






