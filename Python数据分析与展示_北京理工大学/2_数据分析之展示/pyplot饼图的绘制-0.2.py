# -*- pyplot饼图的绘制 -*-
# --0.2--


import matplotlib.pyplot as plt

labels = 'aaa', 'bbb', 'ccc', 'ddd' 
sizes = [ 15, 30, 45, 10 ]
explode = ( 0, 0.1, 0, 0 )

plt.pie( sizes, explode = explode, labels = labels, autopct = ' %1.1f%% ', 
        shadow = False , startangle = 90 )

plt.axis( 'equal' )

plt.show()




