#!/bin/python3

import sys

input = sys.argv

input_num = float(input[1])

while(1.2 <= input_num <= 6.7 or 20.5 <= input_num <=30.6):
	print("Argument in valid range, accepted.")
	exit()
else:
	print("Invalid entry.")
