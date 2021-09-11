#https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
def format_duration(seconds: int)->str:
    if seconds==0:
        return "now"
    time_dictionary = {
        'year': 0,
        'day' : 0,
        'hour' : 0,
        'minute' : 0,
        'second' : 0,
    }
    time_durations = {
        'year' : 365*24*60*60,
        'day' : 24*60*60,
        'hour' : 60*60,
        'minute' : 60,
        'second' : 1,
    }
    remaining=seconds
    for duration in ['year', 'day', 'hour', 'minute', 'second']:
        amount = remaining // time_durations[duration]
        if amount == 0:
            continue
        time_dictionary[duration] = amount
        remaining -= amount * time_durations[duration]
    res=[]

    for duration in ['year', 'day', 'hour', 'minute', 'second']:
        if time_dictionary[duration]!=0:
            if time_dictionary[duration] > 1:
                res.append(f'{time_dictionary[duration]} {duration}s')
            else:
                res.append(f'{time_dictionary[duration]} {duration}')
    if len(res) > 1:
        return ", ".join(res[:-1]) + ' and ' + res[-1]
    return res[0]
print(format_duration(213))
