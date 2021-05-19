#https://www.codewars.com/kata/552c028c030765286c00007d/train/python
def iq_test(numbers):
    numbers=numbers.split()
    even=0
    odd=0
    for num in numbers:
        if (int(num)%2==1):
            odd+=1
        else:
            even+=1
    if odd==1:
        for i in range(len(numbers)):
            if (int(numbers[i])%2==1):
                position=i+1
    else:
        for i in range(len(numbers)):
            if (int(numbers[i])%2==0):
                position=i+1
    return position
