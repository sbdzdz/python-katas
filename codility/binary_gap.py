"""
Given an integer N, Find the longest sequence of consecutive zeros
surrounded by ones at both ends in the binary representation of that integer.
"""

import re

def solution(N):
    binary = "{0:b}".format(N)
    pattern = re.compile('(0+)1')
    lengths = [len(gap) for gap in pattern.findall(binary)]
    return max(lengths) if lengths else 0
