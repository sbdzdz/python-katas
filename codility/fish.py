"""
You are given two non-empty arrays A and B consisting of N integers.
They represent N fish in a river, ordered downstream along the flow of the river.
The fish are numbered from 0 to N-1. If P and Q are two fish and P < Q,
then fish P is initially upstream of fish Q.

Array A contains sizes of the fish, array `B` contains their directions, where:

- 0 represents a fish flowing upstream,
- 1 represents a fish flowing downstream.

Two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0,
and there are no living fish between them. After they meet:

- If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
- If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.

We assume that fish moving in the same direction never meet.
Find the number of fish that will stay alive.
"""

from operator import itemgetter

def solution(A, B):
    stack = []
    for fish in zip(A, B):
        stack.append(fish)
        while len(stack) > 1 and stack[-1][1] == 0 and stack[-2][1] == 1:
            stack.append(max([stack.pop(), stack.pop()], key = itemgetter(0)))
    return len(stack)
