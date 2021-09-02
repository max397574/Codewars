#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
def maskify(cc):
    if len(cc)>4:
        result = ''
        for i in range(len(cc)-4):
            result+='#'
        result+=(cc[-4:])
    else:
        result=cc
    return result
