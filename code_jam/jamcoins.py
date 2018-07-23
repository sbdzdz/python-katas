"""
A jamcoin is a string of N >= 2 digits with the following properties:

- Every digit is either a 0 or 1.
- The first digit is 1 and the last digit is 1.
- If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.

There are communities that use jamcoins as a form of currency. When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10. For convenience, these divisors must be expressed in base 10.

Given J and N, produce J different jamcoins of length N, along with proof that they are legitimate.
"""

import itertools
import collections

def get_nontrivial_divisor(number):
    for i in [2, 3, 5, 7, 11]: # if it's stupid but it works, it's not stupid
        if number%i == 0:
            return i
    return 0

def solution(length, limit):
    jamcoins = []
    for binary in itertools.product(['0', '1'], repeat=length-2):
        binary = "1{}1".format(''.join(binary))
        divisors = []
        for base in range(2, 11):
            divisor = get_nontrivial_divisor(int(binary, base))
            if not divisor:
                break
            divisors.append(divisor)
        else:
            jamcoins.append((binary, divisors))
            if len(jamcoins) == limit:
                break
    return jamcoins

with open('input', 'r') as infile, open('output', 'w') as out:
    next(infile)
    line = next(infile).split()
    length, limit = int(line[0]), int(line[1])
    for binary, divisors in solution(length, limit):
        divisors = list(map(str, divisors))
        out.write("{0} {1}\n".format(binary, ' '.join(divisors)))
