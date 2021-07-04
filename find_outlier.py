# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    returned=0
    odd=0
    even=0
    for int in integers:
        if int%2==0:
            odd+=1
        else:
            even+=1
    if even==1:
        for int in integers:
            if int%2==1:
                return int
    else:
        for int in integers:
            if int%2==0:
                return int
