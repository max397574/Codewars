# https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
def minimum(arr):
    smallest = arr [0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest
def maximum(arr):
    biggest = arr [0]
    for i in arr:
        if i > biggest:
            biggest = i
    return biggest
