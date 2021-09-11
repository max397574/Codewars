#https://www.codewars.com/katadef find_missing(sequence:list):
def find_missing(sequence:list):
    step=int((sequence[len(sequence)-1]-sequence[0])/len(sequence))
    for k in range(1,len(sequence)):
        if sequence[k]-sequence[k-1]!=step:
            return sequence[k-1]+step
