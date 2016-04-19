def solution(S):
    stack = []
    for bracket in S:
        if stack and bracket == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(bracket)
    return int(not stack)