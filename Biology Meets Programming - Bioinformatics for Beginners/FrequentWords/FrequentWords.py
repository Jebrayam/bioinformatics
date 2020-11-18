import biolib as bl

k = 3
text = "CGATATATCCATAG"

def FrequentWords(text, k):
    #list to store most common patterns
    words = []
    #create frequency map with all found patterns
    freq = bl.FrequencyMap(text, k)
    #find maximun values
    m = max(freq.values())
    #iterate through patterns to find m repeated ones
    for key in freq:
        if freq[key] == m:
            words.append(key)
        #end if
    #end for key
    return words

count = FrequentWords(text,k)
print(count)
