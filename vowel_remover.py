def shortcut(s):
    result = ""
    vowels = ["a","e","i","o","u"]
    for c in s:
        if c not in vowels:
            result += c
    return result
