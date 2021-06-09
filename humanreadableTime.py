# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    hours=0
    minutes=0
    while seconds>=3600:
        seconds-=3600
        hours+=1
    while seconds>=60:
        seconds-=60
        minutes+=1
    return("%02d"":""%02d"":""%02d" % (hours, minutes, seconds))
