# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
def array(string):
    list=[]
    list=string.split(',')
    if len(list)<=2:
        return None
    list=list[1:-1]
    strlist= ' '.join(list)
    return strlist
