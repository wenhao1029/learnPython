#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import csv, os
from datetime import datetime

if (__name__ == '__main__'):
	filename = 'd:\python\example1.csv'
	with open(filename, 'r+') as f:
		reader = csv.reader(f)
		header_row = next(reader)
		# print(header_row)
		
		fig = plt.figure()
		ax1 = fig.add_subplot(111)
		
		dates = []
		highs = []
		lows = []
		for row in reader:
			dates.append(datetime.strptime(row[0],"%Y/%m/%d"))
			highs.append(int(row[1]))
			lows.append(int(row[2]))
		
		ax1.set_title("Temperature")
		plt.xlabel("Date", fontsize=14)
		plt.ylabel("Temperature", fontsize=14)
		plt.tick_params(axis='both', labelsize=14)
		
		L1 = ax1.scatter(dates, highs, c='red')
		L2 = ax1.scatter(dates, lows, c='green')
		
		plt.legend([L1, L2], ['Highest', 'Lowest'], loc='upper right')
		# plt.show()
		plt.savefig('d:\python\handleCsvExample.png', bbox_inches='tight')
		