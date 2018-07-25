"""
Find the only element of an array A that occurs odd number of times.
"""

from collections import Counter

def solution(A):
    counter = Counter(A)
    for key, value in counter.iteritems():
        if value%2 != 0:
            return key
