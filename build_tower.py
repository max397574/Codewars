#https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
def tower_builder(n):
    tower=[]
    for i in range(1,n+1):
        tower.append(' '*(n-i)+'*'*(i+(i-1))+' '*(n-i))
    return tower
