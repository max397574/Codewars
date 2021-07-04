# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def count_bits(n):
    binary = str(bin(n)[2:])
    count=0
    for i in binary:
        if int(i)==1:
            count+=1
    return count
