def solution(A, B, K):
    if A%K != 0:
        A = K*((A//K)+1)
    if B%K != 0:
        B = K*((B//K))
    return (B//K)-(A//K)+1
