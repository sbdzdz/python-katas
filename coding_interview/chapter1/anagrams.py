from collections import Counter


def are_anagrams(s1, s2):
    char_range = 255
    counter1 = [0] * char_range
    counter2 = [0] * char_range
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        counter1[ord(c1) - 65] += 1
        counter2[ord(c2) - 65] += 1
    return counter1 == counter2


def are_anagrams_pythonic(s1, s2):
    return Counter(s1) == Counter(s2)
