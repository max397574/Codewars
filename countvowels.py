# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
def get_count(input_str):
    def countX(x,arr):
        count=0
        for i in arr:
            if i==x:
                count+=1
        return count
                
    num_vowels = 0
    num_vowels=num_vowels+countX('a',input_str)
    num_vowels=num_vowels+countX('e',input_str)
    num_vowels=num_vowels+countX('i',input_str)
    num_vowels=num_vowels+countX('o',input_str)
    num_vowels=num_vowels+countX('u',input_str)
    
    return num_vowels
