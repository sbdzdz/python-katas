"""
Given a string S, return the index of a character such that
the part of the string to the left of that character is a reversal 
of the part of the string to its right. Return -1 if no such index exists.
"""

def solution(S):
    if len(S)%2 == 0:
        return -1
    if S == S[::-1]:
        return len(S)/2  
    return -1
