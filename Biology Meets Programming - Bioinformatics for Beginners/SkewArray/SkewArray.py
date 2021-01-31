#SkewArray(Genome) that takes a DNA string Genome as input and returns the skew array of Genome
#in the form of a list whose i-th element is Skew[i]

genome = 'CATGGGCATCGGCCATACGCC'

def SkewArray(genome):
    skew_count = 0
    skew_array = [0]*(len(genome)+1)

    #go throung each nucleotide in the genome
    for i in range(1,len(genome)+1):
        #add one if the nucleotide is G
        if genome[i-1] == 'G':
            skew_count += 1
        #rest one if the nucleotide is C
        elif genome[i-1] == 'C':
            skew_count -= 1
        
        #set the values of skew_count in the skew array
        skew_array[i] = skew_count
    #end for i
    return skew_array

print(SkewArray(genome))

        