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
n_kmer = 0

pos2 = 0

while (pos2 < len(nt)):
	second = nt[pos2]
	pos2 = pos2 + 1
	# make a loop for the third position
	pos4 = 0
	while (pos4 < len(nt)):
		first = nt[args1]
		third = nt[args2]
		fourth = nt[pos4]
		pos4 = pos4 + 1
		print(first, second, third, fourth)
		n_kmer += 1

# print the required text
# then print the total
print("The total number of possibilities is:") 
print(n_kmer)

