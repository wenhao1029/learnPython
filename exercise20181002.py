#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('d:\python\learnPython')
from exercise_class import Restaurant  #Import a local class from a local module
from exercise_class import Car
from exercise_class import ElectricCar

# # restaurant_a = Restaurant('HelloRestaurant', 'Special')#The __init__() with paramters is used.
# restaurant_a = Restaurant()  #The __init__() without paramters is used.

# restaurant_a.describe()
# # restaurant_a.open() 
# restaurant_a.open(10)


# car_audi = Car('audi', '1900', 300)
# # car_audi = Car()
# car_audi.show()
# car_audi.updateOdoMeter(200)
# car_audi.show()


# car_electricA = ElectricCar('audi', '1900', 300, 80)
# car_electricA.show()

# Use member class instance
car_2 = Car('audi', '1900', 300, 2.5)
car_2.show()

car_3 = Car('audi', '1900', 300)
car_3.show()
 