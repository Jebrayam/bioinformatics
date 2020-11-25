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
#finds the more frequent pattern in a sequence
def FrequentWords2(text, k):
    #list to store most common patterns
    words = []
    #create frequency map with all found patterns
    freq = FrequencyMap(text, k)
    #find maximun values
    m = max(freq.values())
    #iterate through patterns to find m repeated ones
    for key in freq:
        if freq[key] == m:
            words.append(key)
        #end if
    #end for key
    return words

######################################################
#find all occurrences of a pattern in a string
def PatternMatching(pattern, genome):
    #empty list to store starting points
    startP = []

    #loop to find pattern through whole genome
    for i in range(len(genome) - len(pattern) + 1):
        #current genome slide
        tempWnd = genome[i:i+len(pattern)]
        #compare current genome slide and pattern
        if tempWnd == pattern:
            startP.append(i)
            
    return ' '.join([str(x) for x in startP])
######################################################
#Find the reverse complement of a DNA string.
#reverse string
def Reverse(pattern):
    return pattern[::-1]

#change nucleotides for complements
def Complement(pattern):
    compR = ''
    for i in pattern:
        temp = ""
        if i == "A":
            temp = "T"
        elif i == "T":
            temp = "A"
        elif i == "C":
            temp = "G"
        elif i == "G":
            temp = "C"
        compR = compR + temp
    
    return compR

#find reverse complement of a pattern
def ReverseComplement2(pattern):
    pattern = Reverse(pattern)
    pattern = Complement(pattern)
    return pattern
#######################################
#find all occurrences of a pattern in a string
def PatternMatching2(pattern, genome):
    #empty list to store starting points
    startP = []

    #loop to find pattern through whole genome
    for i in range(len(genome) - len(pattern) + 1):
        #current genome slide
        tempWnd = genome[i:i+len(pattern)]
        #compare current genome slide and pattern
        if tempWnd == pattern:
            startP.append(i)
            
    return startP
