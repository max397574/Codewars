def countx(x, arr):
    counter=0
    for ele in arr:
        if ele==x:
            counter+=1
    return counter
def find_uniq(arr):
    for x in arr:
        if (countx(x, arr)>1):
            for element in arr:
                if (element!=x):
                    return element
