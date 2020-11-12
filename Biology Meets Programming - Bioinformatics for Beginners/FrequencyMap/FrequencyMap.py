def FrequencyMap(Text, k):
    #creates a dictionary to store pattern counts
    freq = {}
    n = len(Text)
    #ranges through each pattern and counts the number of k-mer
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        #the pattern is comparated with slices of sequences taken
        #from the sequence. if the slice and the pattern are
        #equal, then count increases at one.
        for j in range(0,len(Text) - len(Pattern) + 1):
            if text[j:(j+len(Pattern))] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq


k = 3
text = "CGATATATCCATAG"

freq = FrequencyMap(text, k)
print(freq)
