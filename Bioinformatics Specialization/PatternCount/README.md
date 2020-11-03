# PatternCount Function
**PatternCount(data, pattern)**: Slides a window down *data*, checks whether each k-mer substring of *data* matches *pattern*.

Pseudocode:


    PatternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
                count ← count + 1
        return count
