
# coding: utf-8

# ### Homework 2. Classes.

### Class Kmer
class Kmer:

    def __init__(self,kmer_name):
        self.sequence = kmer_name
        self.loci = [] # list of found loci coordinates
        self.counter = 1 # the number of appearance of kmer in string

    def increase(self):
        self.counter += 1 
        
    def increase_n(self, n):
        self.counter += n
        
    def add_locus(self, chrom, position):
        self.loci.append((chrom, position)) # adding locus start coordinate
        
    def show_loci(self):
        for chrom, position in self.loci:  # show loci source and start coordinate 
            print("{}\t{}".format(chrom, position))
            

seq = open("./seq_y_pestis.fasta", "r")
seq = seq.readlines() # read line by line
seq_name = seq[0].strip() # first line will be a name (at least in our case)
seq2 = "".join(seq[1:1000]).replace('\n', '')
seq_lng = len(seq2)
kmer_size = 23 # set kmer size
kmer_dict = {}
for index in range(seq_lng-kmer_size+1):
    current_kmer = seq2[index:(index+kmer_size)]
    if current_kmer in kmer_dict:
        kmer_dict[current_kmer].increase() #increase counter
    else:
        kmer_dict[current_kmer] = Kmer(current_kmer)
    kmer_dict[current_kmer].add_locus(seq_name, index) # add index and file name
       

max(kmer_dict.values(), key=lambda x: x.counter).loci  # the most common kmer is found twice

max(kmer_dict.values(), key=lambda x: x.counter).show_loci() # its start coordinates





