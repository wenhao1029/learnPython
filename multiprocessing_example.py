#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from multiprocessing import Pool
import os, time, random
import threading
import multiprocessing

# def func_main(name):
	# print("Now it's running the child process %s of id: %s" % (name, os.getpid()))  #get pid of child process
	
	
# if (__name__ == "__main__"):
	# print("It's parent process of id(%d) running!" % os.getpid())
	# p = Process(target=func_main, args=('test',))
	# p.start()
	# p.join()   #To wait for a process to end.
	# print('Child process end.')


# def task_entry(name):
	# print('Running task %s of id %s' % (name, os.getpid()))
	# start=time.time()
	# time.sleep(random.random()*3)
	# end=time.time()
	# print('Task %s running for %0.2f seconds' % (name, end-start))
	
# if (__name__ == '__main__'):
	# print('Parent process %s' % os.getpid())
	# p = Pool(5)
	# for i in range(5):
		# p.apply_async(task_entry, args=(i,))
	
	# print('Wait for all sub processes done!')
	# p.close()# close() must be called before join()
	# p.join() # To wait for all sub processes to be ended.
	# print('All sub processes done!')
	
# def loop():
	# print('Thread %s is running...' % threading.current_thread().name)
	# n = 0
	# while n < 5:
		# n = n + 1
		# print('Thread %s >>> %s' % (threading.current_thread().name, n))
		# time.sleep(1)
	# print('Thread %s ended.' % threading.current_thread().name)
	
# if (__name__ == '__main__'):
	# # print('Thread %s is running...' % threading.current_thread().name)  #A default main thread will be started automatically.
	# # t = threading.Thread(target = loop, name='LoopThread')
	# # t.start()
	# # print('pause here.')  #Till now, the new thread has not been run actually. Only when t.join() is called, the thread will run.
	# # t.join()
	# # print('Thread %s ended.' % threading.current_thread().name)
	
	# print('Number of cores in your computer: %s' % multiprocessing.cpu_count())
	
	
# def loop(): #the thread running this function will be in infinite loop and occupy CPU all the time.
	# x = 0
	# while True:
		# x = x^1
		
# if (__name__ == '__main__'):
	# for i in range(multiprocessing.cpu_count()):
		# t = threading.Thread(target=loop)
		# t.start()
		
		

	
	
	
	

	
	
