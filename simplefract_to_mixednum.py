def mixed_fraction(s):
    num, den = s.split('/')
    num=int(num)
    den=int(den)
    number=num//den
    def gcd(a,b):
        while b!=0:
            c=a%b
            a=b
            b=c
        return a
    num=num%den
    den=den
    greatest=gcd(num,den)
    num=int(num/greatest)
    den=int(den/greatest)
    fract=str(num)+'/'+str(den)
    
    
    if number!=0 and num!=0:
        number=str(number)
        return(number+' '+fract)
    elif num==0:
        return(str(number))
    else:
        number=str(number)
        return(fract)
print(mixed_fraction('-10/7'))
