#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(iterable):
    chars = []
    for i, item in enumerate(iterable):
        if i == 0 or item != iterable[i-1]:
            chars.append(item)
    return chars
