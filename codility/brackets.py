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