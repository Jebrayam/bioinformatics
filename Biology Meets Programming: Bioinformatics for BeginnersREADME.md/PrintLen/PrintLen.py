#loads genomic sequence
data = open('v_cholerae_oric.txt')
text = data.read()
data.close()

#number of nucleotids in the sequence
def PrintLen(data):
    sq_len = len(data)
    print(sq_len)
    
PrintLen(text)