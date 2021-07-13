#https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def is_triangle(a:int,b:int,c:int)->bool:
    if a >= b+c or b >= a+c or c >= a+b:
        return False
    else:
        return True
