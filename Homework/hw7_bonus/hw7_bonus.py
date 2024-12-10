#!/usr/bin/python3

# import arguments
import sys

# rename arguments
range_input = sys.argv[1]
file_in = sys.argv[2]
file_out = sys.argv[3]

# open the range file
range_fh = open(range_input, "r")


# read the range file in 
for range_line in range_fh:
    # open the data file here
    gene_fh = open(file_in, "r")
    
    # isolate the header assign it and print it
    rawheader = gene_fh.readline()
    header = rawheader.rstrip()
    
    # now deal with the actual data
    line = range_line.rstrip()
    rangeparts = line.split("\t")
    
    # assign each range to a name for later referal and float it
    lower_string, upper_string = rangeparts[0:]
    lower_float = float(rangeparts[0])
    upper_float = float(rangeparts[1])
    
    # open the outfile and write the header to it
    outfile_handle = open(f"{file_out}_{lower_string}_{upper_string}_range.txt", "w")
    outfile_handle.write(f"{header}\n")

    # loop through the actual data file 
    for rawline in gene_fh:
        line = rawline.rstrip()
        lineparts = line.split("\t")
        # define liver values as an object for NA filtering
        liver_1 = lineparts[3]
        liver_2 = lineparts[8]
        liver_3 = lineparts[13]
        liver_list = [liver_1, liver_2, liver_3]
        if "NA" not in liver_list:
            #identify the liver values again, float them, and put them in a list
            liver_1_fl = float(lineparts[3])
            liver_2_fl = float(lineparts[8])
            liver_3_fl = float(lineparts[13])
            # put all these values in a list to access
            liver_list = [liver_1_fl, liver_2_fl, liver_3_fl]
            # average the liver values
            liver_avg = (liver_1_fl + liver_2_fl + liver_3_fl)/3
            if lower_float <= liver_avg and upper_float >= liver_avg:
                lineparts[-1] = lineparts[-1] + "\n"
                outfile_handle.write("\t".join(lineparts))
    # close gene file here
    gene_fh.close()
    # close the writing file
    outfile_handle.close()

# print something so the user knows it ran
print(f"Your files have been written :)")