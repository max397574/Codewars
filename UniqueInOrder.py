#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(iterable):
    chars = []
    for i in range(len(iterable)):
        if i == 0 or iterable[i] != iterable[i-1]:
            chars.append(iterable[i])
    return chars
