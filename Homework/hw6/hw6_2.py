#!/bin/python3

# import arguments

import sys

# redefine and exclude the 0th arugument 
INPUT_VAR = sys.argv[1:]

# if there is anything other than three arugments provided
# reject it

num_args = len(INPUT_VAR)
if(not(num_args == 3)):
	print("Three arguments required. Exiting.")
	exit()


for num in INPUT_VAR:
	#convert num to an integer
	num = int(num)
	if(num == 5 or num== 6 or num== 7):
		print(num, "accepted.")
	else:
		print(num, "is an invalid argument, not accepted.")

