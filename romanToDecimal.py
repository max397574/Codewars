#https://www.codewars.com/kata/51b6249c4612257ac0000005
def solution(roman):
    decimal=[]
    summe=0
    for char in roman:
        decimal.append(roman_decimal[char])
    for i in range(len(decimal)-1):
        if decimal[i]<decimal[i+1]:
            summe-=decimal[i]
        else:
            summe+=decimal[i]
    summe+=decimal[-1]
    return summe

roman='XVX'
roman_decimal={ 'X':10, 'I':1, 'V':5, 'L':50, 'C':100, 'D':500, 'M':1000}
print(solution(roman))
