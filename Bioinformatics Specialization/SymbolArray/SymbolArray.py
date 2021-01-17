#symbol array: counts the number of occurences of a symbol in a genome
import biolib as bl


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = bl.PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

genome = 'AAAAGGGG'
symbol = 'A'

print(SymbolArray(genome, symbol))