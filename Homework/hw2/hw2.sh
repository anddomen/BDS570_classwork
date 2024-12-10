#!/bin/bash
# Construct my gene and tissue sample sets
wc -l GeneExprStudy.txt
head -n 25 GeneExprStudy.txt > GeneExprStudy_sample_1.txt
head -n 14 GeneExprStudy.txt > GeneExprStudy_sample_2.txt
tail -n 15 GeneExprStudy.txt > GeneExprStudy_sample_3.txt
head -n 5 GeneExprStudy.txt | cut -f 1-3 > GeneExprStudy_sample_4.txt
head -n 5 GeneExprStudy.txt | cut -f 5,7,12 > GeneExprStudy_sample_5.txt
paste GeneExprStudy_sample_4.txt GeneExprStudy_sample_5.txt > GeneExprStudy_sample_6.txt
