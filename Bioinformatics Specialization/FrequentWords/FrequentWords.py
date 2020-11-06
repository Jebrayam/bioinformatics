#module created through the learning process
import biolib as bl

#loads genomic sequence
data = open('dataset.txt')
seq = data.read()
data.close()

k = 11

def FrequentWords(seq, k):
    #arrays to store frequent patterns
    nameFreq = list()
    countFreq = list()
    #initial maxXount
    maxCount = 0
    #for loop to find maxCount of frequent pattern
    for i in range(len(seq)-k):
        pattern = seq[i:i+k]
        count = bl.PatternCount(seq, pattern)
        
        if count > maxCount:
            maxCount = count
    #end for i
            
    #for loop to find frequen pattern
    for j in range(len(seq)-k):
        pattern = seq[j:j+k]
        count = bl.PatternCount(seq, pattern)
        
        if count == maxCount and pattern not in nameFreq:
            nameFreq.append(pattern)
            countFreq.append(count)
    #end for j
            
    return ' '.join(nameFreq)

print(FrequentWords(seq, k))
        
