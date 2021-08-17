#https://www.codewars.com/kata/5547929140907378f9000039/train/python
def shortcut(s):
    result = ""
    vowels = ["a","e","i","o","u"]
    for c in s:
        if c not in vowels:
            result += c
    return result
