#https://www.codewars.com/kata/58ad317d1541651a740000c5/train/python
import itertools
def middle_permutation(string):
    permutation=list("".join(p) for p in set(itertools.permutations(string)))
    permutation.sort()
    if len(permutation)%2==0:
        return permutation[int(len(permutation)/2-1)]
    else:
        return permutation[int(len(permutation)//2)]
