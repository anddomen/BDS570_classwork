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

# make a for loop that prints T in the first postion, random middle letter,
#then A in the last position
# finally, add a count to length for each loop

for pos2 in range(0, len(nt)):
	second = nt[pos2]
	# make a loop for the third position
	for pos4 in nt:
		first = nt[args1]
		third = nt[args2]
		print(first, second, third, pos4)
		n_kmer += 1

# print the required text
# then print the total
print("The total number of possibilities is:") 
print(n_kmer)

