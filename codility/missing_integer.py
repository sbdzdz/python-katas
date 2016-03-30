from itertools import count

def solution(A):
    A = set(A)
    return next(i for i in count(1) if i not in A)