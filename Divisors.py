#https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python
#TODO: Optimize
def divisors(integer):
    divisor=[]
    for i in range(2,integer-1):
        if integer%i==0:
            divisor.append(i)
    if len(divisor)==0:
        return f'{integer} is prime'
    return divisor
