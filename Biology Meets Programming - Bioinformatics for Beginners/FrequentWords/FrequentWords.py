import biolib as bl

k = 3
text = "CGATATATCCATAG"

def FrequentWords(text, k):
    words = []
    freq = bl.FrequencyMap(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
        #end if
    #end for key
    return words

count = FrequentWords(text,k)
print(count)
