#!/usr/bin/python3

import sys

# assign user inputted data
infile = sys.argv[1]
bins = sys.argv[2]
outfile = sys.argv[3]

# open the bins file
bins_fh = open(bins, "r")

# we need to remove the header 
bin_rawheader = bins_fh.readline()

## PREP WORK FOR BIN LOOP
# make empty lists for the bins
low_list = []
high_list = []
count_list = []

# put in a check for the bin file to make sure the first value is zero
first_bin = True

## BIN LOOP
# start the whole loop by assigning the bin ranges
for bin_line in bins_fh:
    # lets assign the bin numbers
    rangeparts = bin_line.split("\t")
    
    # assign each range to a name
    lower_float = float(rangeparts[0])
    upper_float = float(rangeparts[1])
    
    # Only runs when first_bin is True (first line only)
    if first_bin == True:  
        if lower_float != 0:
            print("ERROR: First bin does not start at zero! Check your bin file.")
        # Switch flag to False so we don't check again
        first_bin = False  # Switch flag to False so we don't check again
    
    # append the empty list
    low_list.append(lower_float)
    high_list.append(upper_float)
    count_list.append(0)

## CREATE PLUS BIN
# now we need to add the "plus" bin, so the last value plus 1
# this high value will live in the low bin
# add an empty value for the high bin
low_list.append(high_list[-1]+1)
high_list.append(float())
count_list.append(0)

# close the bin file
bins_fh.close()
   
## PREP WORK FOR GENE DISTANCE LOOP
# declare empty "previous" lines to use in the loop to compare to
prev_chr = ""
prev_str = ""
prev_start = float()
prev_end = float()

# open the gene annotation data
gene_fh = open(infile, "r")

## GENE DISTANCE CALCULATION LOOP
# loop through the gene file
for raw_line in gene_fh:
    line = raw_line.split("\t")
        
    # assign "current" variables to compare to the previous ones
    current_chr = line[0]
    current_str = line[6]
    current_start = float(line[3])
    current_end = float(line[4])
        
    # now we have to check if the current chr matches the previous chr
    # also make sure the strings match
    if current_chr == prev_chr and current_str == prev_str:
        gene_dist = current_start - prev_end
    
        # take care of the edge cases
        # first take care of the distances that have no distance or a 
        # gene within another gene
        if gene_dist <= 0:
            # add one to the counter
            count_list[0] += 1
            
            # if the current end of the gene is less than the prev
            # its a nested gene so use continue to "skip" that gene
            if current_end < prev_end:
                continue
        
        # now grab the distances that are larger than the bin file lists
        elif gene_dist > low_list[-1]:
            count_list[-1] += 1
        
        # finally, iterate through the rest of the index to get the other bins
        else:
            for index in range(0,len(low_list)):
                # filter through the "normal" gene distances:
                if gene_dist >= low_list[index] and gene_dist <= high_list[index]:
                    count_list[index] += 1
             
    #now update the previous info to the current one
    prev_chr = current_chr
    prev_str = current_str
    prev_start = current_start
    prev_end = current_end

        
# close the gene file    
gene_fh.close()

# make the outfile
outfile_fh = open(outfile, "w")

# make a header for the outfile
outfile_header = "Low\tHigh\tCount\n"

# write the header to the file
outfile_fh.write(outfile_header)

# time to write the file
for i in range(0, len(low_list)):
    values = f"{low_list[i]}\t{high_list[i]}\t{count_list[i]}\n"
    outfile_fh.write(values)
    
# close the exported file
outfile_fh.close()

# let the user know their file is done
print(f"Success! Your histogram is located in {outfile}")