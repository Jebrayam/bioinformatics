#library containing previous implemented functions
#finds how many times there is a pattern in a sequence
def PatternCount(text, pattern):
    count = 0
    #the pattern is comparated with slices of sequences taken
    #from the sequence. if the slice and the pattern are
    #equal, then count increases at one.
    for i in range(0,len(text) - len(pattern) + 1):
        if text[i:(i+len(pattern))] == pattern:
            count += 1
    return count
###############################################################
#finds the more frequent pattern in a sequence
def FrequentWords(seq, k):
    #arrays to store frequent patterns
    nameFreq = list()
    countFreq = list()
    #initial maxXount
    maxCount = 0
    #for loop to find maxCount of frequent pattern
    for i in range(len(seq)-k):
        pattern = seq[i:i+k]
        count = PatternCount(seq, pattern)
        
        if count > maxCount:
            maxCount = count
    #end for i
            
    #for loop to find frequent pattern
    for j in range(len(seq)-k):
        pattern = seq[j:j+k]
        count = PatternCount(seq, pattern)
        
        if count == maxCount and pattern not in nameFreq:
            nameFreq.append(pattern)
            countFreq.append(count)
    #end for j
            
    return ' '.join(nameFreq)
###################################################################
#creates a map (dictionary) with a set of patterns and its corresponding k-mer counts
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        #the pattern is comparated with slices of sequences taken
        #from the sequence. if the slice and the pattern are
        #equal, then count increases at one.
        for j in range(0,len(Text) - len(Pattern) + 1):
            if Text[j:(j+len(Pattern))] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq
################################################################
#reverses a sequence patterns
def ReverseComplement(pattern):
    rev_pattern = ""
    for i in pattern[::-1]:
        temp = ""
        if i == "A":
            temp = "T"
        elif i == "T":
            temp = "A"
        elif i == "C":
            temp = "G"
        elif i == "G":
            temp = "C"
        rev_pattern = rev_pattern + temp
    return rev_pattern
################################################################
