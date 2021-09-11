#https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
def narcissistic(value):
    str_value = str(value)
    total = 0
    for num in str_value:
        total+=pow(int(num),len(str_value))
    if total == value:
        return True
    return False
