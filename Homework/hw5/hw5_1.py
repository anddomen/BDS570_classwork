#!/bin/python3

# import arguments

import sys

# redefine
args = sys.argv

# define the acceptable list
organs = ["Liver", "Kidney", "Heart", "Brain"]

# assign a name to the arguments
INPUT_VAR = args[1]

# if args is in organs, print this
# elsif print this

if (INPUT_VAR in organs):
	print("Performing test on", INPUT_VAR)
	exit()
else: print("Invalid Tissue. Valid tissues are: Liver, Kidney, Heart, or Brain. Exiting.")

