#loads genomic sequence
data = open('dataset_2_7.txt')
text = data.read()
data.close()

# text = 'GCGCG'
#pattern to look for throughout the sequence
pattern = 'GCG'

def PatternCount(text, pattern):
    count = 0
    #the pattern is comparated with slices of sequences taken
    #from the sequence. if the slice and the pattern are
    #equal, then count increases at one.
    for i in range(0,len(text) - len(pattern) + 1):
        if text[i:(i+len(pattern))] == pattern:
            count += 1
    return count

#calls PatternCount function
nSeq = PatternCount(text, pattern)
#prints result
print(nSeq)
