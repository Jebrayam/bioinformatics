#convert number to pattern

number = 5437
k = 8

def NumberToPattern(number, k):
    #list with numcleotides. Each index correspont to its own number
    nucleotides = ['A', 'C', 'G', 'T']
    
    #empty string to concatenate nucleotides
    pattern = ''
    
    temp = number
    for i in range(k):
        #the residual values are the number used to convert to pattern
        numb_nucle = temp % 4
        #temporal value of the input number
        temp = temp//4
        #concatenate string of nucleotides
        pattern = nucleotides[numb_nucle] + pattern
    
    return pattern

print(NumberToPattern(number,k))