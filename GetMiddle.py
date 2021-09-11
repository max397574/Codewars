#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    middle=len(s)//2
    if len(s)%2==1:
        return s[middle]
    return s[middle-1:middle+1]
