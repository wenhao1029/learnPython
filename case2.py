#!/usr/bin/env python3
# -*- coding: utf-8 -*-

linesList = []
try:
	with open('d:\python\learnPython\example2.txt') as file_ob:
		linesList = file_ob.readlines()
except FileNotFoundError:
		msg = "Sorry, the file " + "example1.txt" + " does not exist!"
		print(msg)

print(len(linesList))
		
for line in linesList:
	print(line.rstrip())

# Check if a string is in the file.
i=0
for line in linesList:
	i +=1
	if "fd" in line:
		print("found in line %d" % i)
		break
