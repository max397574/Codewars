# https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes
 
primes = SieveOfEratosthenes(10000)
def total(arr):
    sum=0
    for i in range(len(arr)):
        if i in primes:
            sum+=arr[i]
    return sum
