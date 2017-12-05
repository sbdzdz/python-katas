import inputs
import math

def no_duplicates(p):
    p = p.split()
    return  len(p) == len(set(p))

def no_anagrams(p):
    p = p.split()
    sets = [''.join(sorted(word)) for word in p]
    return  len(sets) == len(set(sets))

part_one = len([p for p in inputs.passphrase.split('\n') if no_duplicates(p)])
part_two = len([p for p in inputs.passphrase.split('\n') if no_anagrams(p)])

print(part_one, part_two)
