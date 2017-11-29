#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


if (__name__ == '__main__'):
	input_values=[1,2,3,4,5]
	squares = [1,4,9,16,25]
	# plt.plot(input_values, squares, 'rD-', label='Squared_value')
	# plt.plot(input_values, squares, color='green', linestyle='dashed', marker='D', markerfacecolor='blue', markersize=12)
	plt.title("Square Number", fontsize=24)
	plt.xlabel("Value", fontsize=14)
	plt.ylabel("Square of value", fontsize=14)
	plt.tick_params(axis='both', labelsize=14)
	# plt.show()
	
	plt.scatter(input_values, squares, c='red', edgecolor='none', marker='D', s=14)
	plt.axis([0,10,0,100])
	# plt.show()
	plt.savefig('d:\python\matplotexample.png', bbox_inches='tight')
	