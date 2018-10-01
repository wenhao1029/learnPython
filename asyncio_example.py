#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

@asyncio.coroutine

def hello1():
	print('Hello world -- 1! (%s)' % threading.currentThread())
	yield from asyncio.sleep(10) # It will stop executing in this hello(), and start run another task in the loop. asyncio.sleep() is also a coroutine.
	print('Hello again -- 1! (%s)' % threading.currentThread())
	
def hello2():
	print('Hello world -- 2 ! (%s)' % threading.currentThread())
	yield from asyncio.sleep(10) # It will stop executing in this hello(), and start run another task in the loop.asyncio.sleep() is also a coroutine.
	print('Hello again -- 2! (%s)' % threading.currentThread())
	
def hello3():
	print('Hello world -- 3 ! (%s)' % threading.currentThread())
	yield from asyncio.sleep(10) # It will stop executing in this hello(), and start run another task in the loop.asyncio.sleep() is also a coroutine.
	print('Hello again -- 3! (%s)' % threading.currentThread())
	
loop = asyncio.get_event_loop()
tasks = [hello1(), hello2(), hello3()]

loop.run_until_complete(asyncio.wait(tasks))  # put a list of tasks into the loop and run it.
loop.close  

# The total executing time is not 30 second. It's just around 10 seconds. So hello(), hello2(), hello3() and asyncio.sleep are all executed parallelly.
# asyncio.sleep() can be replaced as real IO operation