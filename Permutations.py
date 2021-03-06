#https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
def permutations(string: str)->list:
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])
    elif len(string) > 2:
        for i, c in enumerate(string):
            for s in permutations(string[:i] + string[i + 1:]):
                result.add(c + s)
    return list(result)
print(permutations('ABC'))
