# BDS 547 Classwork

#### Description:

This repository is for my homework and project code from BDS 570 at Oregon State. The homework code does not have any accompanying documentation, but the project shell script has a detailed explanation on what is needed to run the script as well as example annotation data. This class was my first time coding in Python for any significant amount of time, so my code is likely inelegant at this point, but it all works at least.

#### Project details:

The project was the culmination of the things we had learned all term. I chose the project option that calculated the intergenic distances from a sorted .gff file and creates a histogram using a user-defined bin file. If there is an overlapping or nested gene, the program accounts for this by declaring it as a "zero distance", while also correctly calculating the next gene distance. It will only calculate distances assuming the chromosome number and strand (+/-) match.

For more details on running this script, please consult the ./gene_annot.sh file.

**NOTE**: If you are a student that came across this by some clever googling, make sure to try completing the homework/project on your own. I promise you won't learn anything if you just copy mine.
