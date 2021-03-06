#find all occurrences of a pattern in a string
pattern = "ATAT"
genome = "GATATATGCATATACTT"

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
            
    return startP

print(PatternMatching(pattern, genome))