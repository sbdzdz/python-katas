from collections import Counter

def solution(N):
    counter = Counter(N)
    for key, value in counter.iteritems():
        if value%2 != 0:
            return key
