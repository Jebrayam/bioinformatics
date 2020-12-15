#Convert pattern to number

pattern = "ATGCAA"

def PatternToNumber(pattern):
    # return the index of the pattern in the frequency array
    nucleotides = dict(A=0, C=1, G=2, T=3)
    k = len(pattern)
    i = k - 1  # start from the last nucleotide
    result = 0

    while i >= 0:
        nucleotide = pattern[(k - 1) - i]
        nucleotide_val = nucleotides[nucleotide]
        result += nucleotide_val * (4 ** i)
        i -= 1
    return result

print(PatternToNumber(pattern))

