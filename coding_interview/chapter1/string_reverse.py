def reverse_cstyle(s):
    if len(s) < 2:
        return s
    r = ''
    for c in s[:-1]:
        r = c+r
    return r + s[-1]

def reverse_cstyle_pythonic(s):
    if len(s) < 2:
        return s
    return s[:-1][::-1] + s[-1]

def reverse_cstyle_while(s):
    if len(s) < 2:
        return s
    r = ''
    i = len(s)-2
    while i >= 0:
        r += s[i]
        i -= 1
    return r + s[-1]
