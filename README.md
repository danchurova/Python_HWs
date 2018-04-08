# Python_HWs
homeworks of the second semester on Python in Bioinformatics Institute 2018

* **HW2** - first Class creation: ```class Kmer``` is a class, whose instances contain sequence, counter - number of appearance of a kmer in reference sequence, loci - start coordinates of kmer appearance in reference sequence. 
* **HW3** - second class - ``` class Kmer_spectrum``` , wchich is analysing fixed-sized kmer spectrum of a fastq file, makes a filtration by a given quality threshold and allows to represent kmer repertoires in a different ways, also calculate genome_size and build a graph of kmer distribution.
* **trimmik** - smoker's variant of a Trimmomatic. gets arguments such as headcrop, tailcrop and just cuts according to quality and window with threshold - scan with a window and delete substring if a mean of phred_quality of this window less than threshold.
