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
            if text[j:(j+len(Pattern))] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq


k = 3
text = "CGATATATCCATAG"

freq = FrequencyMap(text, k)
print(freq)
