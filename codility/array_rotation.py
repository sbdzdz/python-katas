"""
Given a non-empty array, return that array shifted to the right by k indices.
"""

def solution(arr, k):
    rotated = [0] * len(arr)
    for index, element in enumerate(arr):
        rotated[(index+k) % len(arr)] = element
    return rotated
