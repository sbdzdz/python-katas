"""
There are N discs on a plane, numbered from 0 to N-1.
You are given an array A of N non-negative integers.
The J-th disc is drawn with its center at (J, 0) and radius A[J].
Two disc intersect if they have at least one common point (including the border).
Write a function that returns the number of unordered pairs of intersecting discs.
The function should return −1 if the number of intersecting pairs exceeds 10M.
"""

def solution(A):
    discs = []
    count = 0
    open_discs = 0
    for center, radius in enumerate(A):
        discs.append((center-radius, -1))
        discs.append((center+radius, 1))
    discs = [disc[1] for disc in sorted(discs)]
    for element in discs:
        if element == -1:
            count -= open_discs
        open_discs += element
    return count if count <= 10**7 else -1
