#https://www.codewars.com/kata/5842df8ccbd22792a4000245
import math
def expanded_form(num):
    if str(num%10)!='0':
        output=str(num%10)
    else:
        output=''
    factor=10
    while num > 10:
        num=math.floor(num/10)
        if str((num%10)*factor)!='0':
            if output!='':
                output=str(((num%10)*factor))+' + '+output
            else:
                output=str(((num%10)*factor))
        factor*=10
    return output
num=7300000
print(expanded_form(num))
