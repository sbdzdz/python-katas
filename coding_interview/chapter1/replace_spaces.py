def replace_spaces(s):
    r = ''
    for c in s:
        if c == ' ':
            r += '%20'
        else:
            r += c
    return r

def replace_spaces_pythonic(s):
    return s.replace(' ', '%20')
