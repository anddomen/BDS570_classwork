#!/usr/bin/python3

# list nucleotides
nt = ["A", "C", "T", "G"]

# make sure it works
#print(nt)
#print(nt[2])

#make an empty vector to add to to find the nrow of the loop
length = 0

# make a for loop that prints T in the first postion, random middle letter,
#then A in the last position
# finally, add a count to length for each loop

for i in range(0, len(nt)):
	first = nt[2]
	second = nt[i]
	third = nt[0]
	print(first, second, third)
	length += 1

# print the required text
# then print the total length on a new line
print("The total number of possibilities is:")
print(length)
