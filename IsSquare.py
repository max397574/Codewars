#https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
from math import sqrt
def is_square(n:int)->bool:
    return n > -1 and sqrt(n).is_integer()
