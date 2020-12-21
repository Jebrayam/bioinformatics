# NumberToPattern function
**NumberToPattern(index, k)**: Transforms an integer between 0 and 4^k - 1 into a k-mer.

*Pseudocode:*

    NumberToPattern(index, k)
        if k = 1
            return NumberToSymbol(index)
        prefixIndex ← Quotient(index, 4)
        r ← Remainder(index, 4)
        symbol ← NumberToSymbol(r)
        PrefixPattern ← NumberToPattern(prefixIndex, k − 1)
        return concatenation of PrefixPattern with symbol
