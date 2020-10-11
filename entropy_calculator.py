# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#   A script for solving entropy for decision tree problems.                      #
#   Pass value pairs as arrays.                                                   #
#   Ex. calculate([1, 3], [8,0], [7,1])                                           #
#                                                                                 #
#   Author: Tyler Hooks                                                           #
#                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import math

def calculate(*values):
	total = 0
	entropy = 0
	for val in values:
		for v in val:
			total += v
	for val in values:
		probability = sum(val)/total
		for v in val:
			try:
				p = v/sum(val)
				entropy += probability * p * math.log(p, 2)
			except ValueError:
				entropy += 0
	entropy *= -1
	return float("{0:.3f}".format(entropy))
