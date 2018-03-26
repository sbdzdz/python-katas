def unique_characters(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

def unique_characters_pythonic(s):
    return len(set(s)) == len(s)
