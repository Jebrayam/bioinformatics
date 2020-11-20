#Find the reverse complement of a DNA string.
pattern = "AAAACCCGGT"

def Reverse(pattern):
    return pattern[::-1]

def Complement(pattern):
    compR = ''
    for i in pattern:
        temp = ""
        if i == "A":
            temp = "T"
        elif i == "T":
            temp = "A"
        elif i == "C":
            temp = "G"
        elif i == "G":
            temp = "C"
        compR = compR + temp
    
    return compR

def ReverseComplement(pattern):
    pattern = Reverse(pattern)
    pattern = Complement(pattern)
    return pattern

revComp = ReverseComplement(pattern)
print(revComp)
        
        