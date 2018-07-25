"""
Calculate the first n digits of π using a spigot algorithm. 
"""

from math import floor

def print_pi(decimal_places):
    for digit in generate_pi(decimal_places):
        print(digit, end='', flush=True)

def generate_pi(n):
    predigits = []
    mixed = get_mixed_radix_representation(n)
    for i in range(n):
        mixed = regularise(mixed) 
        predigit, mixed[0] = divmod(mixed[0], 10)
        if (predigit != 9 and predigit !=10):
            yield from predigits
            predigits = []
            predigits.append(predigit)
        elif predigit == 9:
            predigits.append(predigit)
        else:
            predigits = [(predigit+1)%9 for predigit in predigits]
            yield from predigits
            predigits = [0]

def get_mixed_radix_representation(n):
    return [2]*floor(10*n/3+1)

def regularise(mixed):
    mixed = [10*x for x in mixed]
    for index in range(len(mixed)-1, 0, -1):
        quotient, remainder = divmod(mixed[index], 2*index+1)
        mixed[index] = remainder
        mixed[index-1] += quotient*max(1, index)
    return mixed

print_pi(1000)
