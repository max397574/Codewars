# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string):
    result = ""
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for c in string:
        if c not in vowels:
            result += c
    return result
