# ComputingFrequencies function
**ComputingFrequencies(Text, k)**: Generates a frequency array.

*Pseudocode:*
    ComputingFrequencies(Text, k)
        for i ← 0 to 4k − 1
            FrequencyArray(i) ← 0
        for i ← 0 to |Text| − k
            Pattern ← Text(i, k)
            j ← PatternToNumber(Pattern)
            FrequencyArray(j) ← FrequencyArray(j) + 1
        return FrequencyArray
