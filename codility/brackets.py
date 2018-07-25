"""
A string S is considered to be properly nested if any of the following is true:

* S is empty;
* S has the form (U) or [U] or {U} where U is a properly nested string;
* S has the form VW where V and W are properly nested strings.

Write a function that returns 1 if S is properly nested and 0 otherwise.
"""

def matching(left, right):
    return (left, right) in [('(', ')'), ('[', ']'), ('{', '}')]

def solution(S):
    stack = []
    for bracket in S:
        if not stack or not matching(stack[-1], bracket):
            stack.append(bracket)
        else:
            stack.pop()
    return int(not stack)
