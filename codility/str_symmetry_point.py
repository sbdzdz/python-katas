def solution(S):
    if len(S)%2 == 0:
        return -1
    if S == S[::-1]:
        return len(S)/2  
    return -1
