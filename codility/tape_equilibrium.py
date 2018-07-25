"""
Find an integer P that splits a array A into two non-empty parts:

A1=A[0], ..., A[P-1] and A2=A[P], ..., A[N-1]

so that the absolute difference between sum(A1) and sum(A2) is minimal.

Return that difference
"""

def solution(A):
    differences = []
    left = 0
    right = sum(A)
    for element in A[:-1]:
        left += element
        right -= element
        differences.append(abs(left - right))
    return min(differences)
