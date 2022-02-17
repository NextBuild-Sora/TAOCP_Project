

# ---* 类的继承机制 *--- #



class Car:
    def __init__(self, name):
        self.name = name
        self.remain_mile_ = 0
        
    def fill_fuel(self, miles):     #加燃料里程
        self.remain_mile = miles
        
    def run(self, miles):     #跑miles英里
        print (self.name, end = ': ' )
        if self.remain_mile >= miles:
            self.remain_mile -= miles
            print( "run %d miles! " % (miles, ) )
        else:
            print("fuel out!")
 
 
class GasCar(Car):
    def fill_fuel(self, gas):     #加汽油gas升
        self.remain_mile = gas * 6.0      #每升跑6英里


class ElecCar(Car):
    def fill_fuel(self, power):     #充电power度
        self.remain_mile = power * 3.0     #每度电3英里
        

gcar = GasCar( "BMW" )
gcar.fill_fuel( 50.0 )
gcar.run( 200.0 )

ecar = ElecCar( "Tesla" )
ecar.fill_fuel( 60.0 )
ecar.run( 200.0 )

