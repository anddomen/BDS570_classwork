#!/usr/bin/python3

# import sys for arugments and rename it for easier access
import sys
args = sys.argv


# list nucleotides
nt = ["A", "C", "T", "G"]

# classify arguments as index
args1 = nt.index(args[1])
args2 = nt.index(args[2])

#make an empty vector to add to to find the nrow of the loop
length = 0

# make a for loop that prints T in the first postion, 
#random middle letter,
#then A in the last position
# finally, add a count to length for each loop

for i in range(0, len(nt)):
	first = nt[args1]
	second = nt[i]
	third = nt[args2]
	print(first, second, third)
	length += 1

# print the required text
# then print the total
print("The total number of possibilities is:") 
print(length)
