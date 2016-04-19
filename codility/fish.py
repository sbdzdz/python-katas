from operator import itemgetter

def solution(A, B):
    stack = []
    for fish in zip(A, B):
        stack.append(fish)
        while len(stack) > 1 and stack[-1][1] == 0 and stack[-2][1] == 1:
            stack.append(max([stack.pop(), stack.pop()], key = itemgetter(0)))
    return len(stack)