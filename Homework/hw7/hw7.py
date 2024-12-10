#!/usr/bin/python3

# import arguments
import sys

# rename arguments
file_in = sys.argv[1]
file_out = sys.argv[2]


# import the file
df = open(file_in, "r")

# isolate the header and assign it
rawheader = df.readline()

# remove the blank parts with rstrip
header = rawheader.rstrip()

# open the output file and write the header to the file
outfile_handle = open(file_out, "w")
outfile_handle.write(f"{header}\n")

# testing, remove or comment when done
#print(header)

# make a for loop to go through each line and apply the appropriate filters

for rawline in df:
	line = rawline.rstrip()
	# put data from line into a list using the tsv
	lineparts = line.split("\t")
	# make readable filter objects
	in_blood = lineparts[1]
	all_values = lineparts[0:]
	# remove things not expressed in blood and NA values
	if (in_blood == "Y" and "NA" not in all_values):
	        # make readable kidney values
		kidney_1 = float(lineparts[6])
		kidney_2 = float(lineparts[11])
		kidney_3 = float(lineparts[16])
		# filter out kidney expressions <1.5
		if (kidney_1 <= -1.5 and kidney_2 <= -1.5 and kidney_3 <= -1.5):
			#identify the liver values and put them in a list
			liver_1 = float(lineparts[3])
			liver_2 = float(lineparts[8])
			liver_3 = float(lineparts[13])
			# put all these values in a list to access
			liver_list = [liver_1, liver_2, liver_3]
			# last filter
			if any(value > 2.0 for value in liver_list) and all(value > 1.5 for value in liver_list):
				lineparts[-1] = lineparts[-1] + "\n"
				# write the resulting filtered data
				outfile_handle.write("\t".join(lineparts))

outfile_handle.close()
df.close()
print(f"The output is written to {file_out}.")

