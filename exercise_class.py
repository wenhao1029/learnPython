#!/usr/bin/env python3
# -*- coding: utf-8 -*-



		
class Restaurant():
	"""A class of Restaurant"""
	
	def __init__(self,name,type):
		self.restaurant_name = name
		self.cuisine_type = type
		
	#means __init__() can be overloaded.
	def __init__(self):  
		self.restaurant_name = "None"
		self.cuisine_type = "None"
		
	def describe(self):
		print("Restaurant's name is " + self.restaurant_name)
		print("Restaurant's cuisine_type is " + self.cuisine_type)
		
	def open(self):
		print("Restaurant is now open!")
		
	# Doesn't support overload for user-defined function very well.	
	def open(self, daysNo):
		print("Restaurant will be open for "+str(daysNo)+" days!")
		
class Engine():

	def __init__(self, volume=2.5):
		self.volume = volume
		
	def show(self):
		print("The engine volume is " + self.volume)
		
				
class Car():
	model = "None"  #Member variable, with default value.
	year = "2000"   #Member variable, with default value.
	odoMeter = 0    #Member variable, with default value.
	
	def __init__(self,model,year,odoMeter = 0, volume=2.0 ):  #odoMeter is a parameter with default value.
		self.model = model
		self.year = year
		self.odoMeter = odoMeter
		self.battery = Engine(volume)
		
	# def __init__(self):  #if no parameters input, this will be called.
		# print("Default __init__ is called.")
		
	def show(self):
		print(self.model + " " + self.year + " with meter " + str(self.odoMeter))
		print("Engine volume is " + str(self.battery.volume))
		
	def updateOdoMeter(self,newMeter):
		if(newMeter < self.odoMeter):
			print("You cann't roll back odoMeter!, current meter is " + str(self.odoMeter))
		else:
			self.odoMeter = newMeter
			print("odoMeter updated with " + str(newMeter))
			
			
class ElectricCar(Car):

	def __init__(self, model,year,odoMeter,power):
		super().__init__(model,year,odoMeter)  #call function of super class
		self.power=power
		
	def show(self):
		super().show() #call function of super class
		print("Power left is " + str(self.power) + "%")
		

		
		

	
	
		
	
	