#!/usr/bin/bash

# This script is to call the program that generates a histogram of intergenic gene distances

### WHAT IS NEEDED TO RUN ###
# 1. A sorted gene annotation file in .gff format which has the chromosome, strand, and gene start

# 2. A tab-delimited file defining the desired bin distances. **NOTE** this file MUST start with a bin of zero and have a complete last line. This is an example of a properly formatted bin distance file:
#Low     High
#0       99
#100     199
#200     299
#300     399
#400     499

# 3. An output file name ending in .txt

### HOW TO RUN ###
# The program takes three arguments (related to the requirements above). The first is your gene file, second is the tab-delimited distances, and the third is what you want your output file to be.

# What it should look like:
# ./gene_annot.py "SORTED_GENE_ANNOTATION_FILE" "BIN_FILE" "OUTPUT_FILE"

# When putting in arguments, use the absolute or relative path to your input files in quotes. Similarly, use the absolute or relative path to where you want your output files to go (also in quotes). If you want your output file to spit out in your current directory, just put the file names in quotes like this: "my_output_file.txt"

# **NOTE**: do not use spaces or special characters in your output name!

# To make it easier, use the pre-formatted execution here:

./gene_annot.py "/home/domena/hub_data_share/data/project_datafile_unique_sets/Gene_Annotation/set_5_annotation.gff" "bins.txt" "gene_annot_hist.txt"

# finally, call this script to run it from the command line by typing ./gene_annot.sh