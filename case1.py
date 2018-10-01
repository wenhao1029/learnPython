#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("Please input your name:")
# name=input("Please input your name:")
# print("hello",name,"!")
# print("Hello Toby!")
# print("Hello world!\n")

# print("你好")

#使用缩进
# a=100
# if a>=100:
	# print(a)
# else: 
	# print(-a)
	
# ##list和tuple使用
# people = ['Toby','Lucy']
# print(people)

# # people = 1  #python 变量类型可随时改变, 那之前分配的内存怎么释放呢？（用来存储list的）
# # print(people)	

# people.append('Gege') #追加元素
# print(people)

# people.pop(1)     #删除元素1,Index from 0
# print(people)

# people[1]='Lucy2'  #修改元素值
# print(people)

# print(len(people))#number of elements in list.

#slice of list.
# L = list(range(100)) # list() is similar with construction fucntion of C++.
# print(L)
# print(L[0:10]) #slice
# print(L[:10]) # index 0 can be omitted.
# print(L[-10:-1])# index -1 means the last element in the list. -2 means the last second element...
# print(L[-10:]) 
# print(L[:]) #exactly same as L
#print(L[10:10]) # return error because index incorrect. start number must be lower than stop number.

# #Check if a list is empty
# L2 = []
# if(L2):
	# print("It's not an empty list!")
# else:
	# print("It's an empty list!")
	
# if(len(L2)):  #another way to check if a list is empty.
	# print("It's not an empty list!")
# else:
	# print("It's an empty list!")
	
# Copy list
# La = ['a', 'b', 'c']
# Lb = La #Not really a copy for content. Like a pointer.
# La.append('d')
# print('La is: ' , La)
# print('Lb is: ' , Lb)  #Lb actually refers to the same list as La. So here Lb is not a new list.

# Lb = La[:]
# La.append('e')
# print('La is: ' , La)
# print('Lb is: ' , Lb)  #Lb now is a new list because we use Lb = La[:] to create and copy from a list.

# # Copy of variable
# a = 1
# b = a
# a += 1
# print(a)
# print(b)   #b is a new variable. even value of a is changed, value of b is kept.



##slice of tuple. tuple is also a kind of list, which can't be changed.
# t = tuple(range(100))
# print(t)
# # t[1]=3 #Error,tuple doesn't support item assignment.
# print(t[1]) #but an item in a tuple can be read.
# print(t[:10])

##slice of str. str is also a kind of list.
# s = str('ABCDEFG') #define and initialize a str.
# print(s)
# print(s[:3])
# print(s[::2]) #2 means the step.'ACEG' will be printed out.


# t = (1,) #A tuple with only one element.
# print(t)
# print(len(t))
# #t.append(2) #Can't append to a tuple
# print(t)

##Usage of loop
# names = ['Toby','Kite','Lucy',3]
# for name in names:  #':' is needed here. Just like if.
	# print(name)
	
# sum = 0
# for x in range(0,102,2): # range(N)返回list = [0,1,...,N-1], range(start,end,interval) returns a Int List, starting from start, ending before end, with interval.
    # sum = sum + x
    # print(x)
	
# print(sum)
# print(range(101)) #Cannot print a list directly??
# print(list(range(101))) # This is OK
# print(range(0,101,2)) #Cannot print a list directly??
# print(list(range(0,101,2))) # This is OK

# ListA = ["a",2]
# print(ListA)

# sum = 0
# n = 99
# while n > 0:
    # sum = sum + n
    # n = n - 2
# print(sum)

##dict
# d={'Toby':95,'Lucy':88} 
# # print(d['Toby'])  #Toby is te key
# # print(d['Simon']) #Error, no such key

# if ('Toby' in d):  #Check if the key exist firstly.
	# print(d['Toby'])
	
# print(d.get('Toby'))	#use method get()
# print(d.get('Simon'))   #No Simon in the dict, so return None.
# print(d.get('Simon',-1)) #if Simon doesn't exist,return -1.

# dNameScore = {10.0:90,'Lucy':80} #any other way to initialize a dict?
# print(dNameScore)
# print(dNameScore[10.0])
# print(dNameScore.items())
# print(dNameScore.keys())
# print(dNameScore.values())
# # print(dNameScore.popitem()) #remove the first pair in the dict.
# # print(dNameScore.popitem())
# # print(dNameScore.popitem()) #report error because the dict is  empty
# dNameScore['Linda'] = 88  #Can insert a new <key,value> into the dict.
# print(dNameScore)
# # print(dNameScore['ErrorName']) #will report error.
# print(dNameScore.__sizeof__())

# dd = {'a':1,'b':2,'c':3}
# for i in dd:
	# print(i)  #will print b, c, a.


##set, set represented by {}.
# s=set([1,2,3]) # consruct a set with a list.
# print(s)
# print(s[0]) #Error, set doesn't support indexing.
# s=set((3,2,1)) #Error, not ok to cunstrct a set with a touple?? strange!
# print(s)

# s1 = set([1])
# s2 = set([2])

# print(s1 & s2)  # print set() means empty set.
# print(s1 | s2)  # print {1,2}

##function
# def abs(x):  #what's the return type??
	# if x>0:
		# return x
	# elif x==0:
		# return 'x'
	# else:
		# return -x
		
# print(abs(-12))
		
# def add_end(L=[]):
	# L.append('END')
	# return L

# print(add_end()) # Default arg is used in function. print ['END']
# L = [1,2,3]
# add_end(L)
# print(L)
# add_end(L)
# print(L)

## List comprehensions
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s,str)]   #generate a lit from L1's elements that are Str.
# print(L2)

# L3 = [x*x for x in range(10)]  #generate list of [1,4,9...]
# print(L3)

# ## Generator
# G1 = (x*x for x in range(10))
# print(G1)  # It doesn't print the list for the moment. Must use next() method, or for loop.
# for g in G1:
	# print(g)
	
## Generator definition in function way
## function type of generator is used to generate complicated list according some logic.(杨辉三角之类)
          # 1
        # 1   1
      # 1   2   1
    # 1   3   3   1
  # 1   4   6   4   1
# 1   5   10  10  5   1
# It's hard to generate this kind of list using normal list generator.

# A function with key word yield is a special function. It's actually a generator.
# When calling this function, it will not be executed actually.
# But calling next() or using for loop to iterate it, the function will be executed and stop in the yield statement.
# def odd():    # A function with yield statement.
	# print("step1")
	# yield 1
	# print("step2")
	# yield 3
	# print("step3")
	# yield 5
	
# oList = odd() # Function will not be executed actually. This is to instantiate a generator instance.
# for o in oList:
	# print(o) # In each loop, function will be executed until a new yield.
	
	
# def yhsj(Max):
	# n=0
	# while(n<Max):
		# tempList2=[]
		# x=0
		# while(x<=n):
			# if((x==0)or(x==n)):
				# tempList2.append(1)
			# else:
				# tempList2.append(tempList[x-1]+tempList[x])
			# x=x+1
		# tempList=tempList2
		# yield tempList

		# n=n+1

# yhsj_inst = yhsj(10)

# for i in yhsj_inst:
	# print(i)


# from datetime import datetime
# now = datetime.now()
# print (now)
# print (type(now))	

# import this

## Modify list in a function
# def sortList(unsortedList):
	# unsortedList.sort()  #The inputed list is changed. After return from this function, change is still kept.
	
# unsortedList = ['a','c','b']
# print(unsortedList)
# sortList(unsortedList)
# print(unsortedList)


def increament(a):
	a+=1
	
a=1
print(a)
increament(a)  #Different with list, a normal variable will not be changed by function calling.
print(a)  # a is still 1.






	










	
	


