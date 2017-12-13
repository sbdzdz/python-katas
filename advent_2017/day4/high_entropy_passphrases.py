import math

def no_duplicates(p):
    p = p.split()
    return  len(p) == len(set(p))

def no_anagrams(p):
    p = p.split()
    sets = [''.join(sorted(word)) for word in p]
    return  len(sets) == len(set(sets))

with open('input') as f:
    inp = f.readlines()

part_one = len([p for p in inp if no_duplicates(p)])
part_two = len([p for p in inp if no_anagrams(p)])

print(part_one, part_two)
