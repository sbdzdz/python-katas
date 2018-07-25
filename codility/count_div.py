"""
Compute the number of integers divisible by k in range [a, b].
"""

def solution(a, b, k):
    if a%k != 0:
        a = k*(a//k + 1)
    if b%k != 0:
        b = k*(b//k)
    return b//k - a//k + 1
