# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python
def is_merge(s, part1, part2):
    def countX(x, arr):
        count=0
        for i in arr:
            if i==x:
                count+=1
        return count
