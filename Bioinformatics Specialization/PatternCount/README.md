# PatternCount Function
**PatternCount(data, pattern)**: Slide a window down *data*, check whether each k-mer substring of *data* matches *pattern*.
PatternCount(Text, Pattern)
    count ← 0
    for i ← 0 to |Text| − |Pattern|
        if Text(i, |Pattern|) = Pattern
            count ← count + 1
    return count
