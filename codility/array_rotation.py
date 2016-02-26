def solution(A, K):
    rotated = [0]*len(A)
    for index, element in enumerate(A):
        rotated[(index+K)%len(A)]=element
    return rotated
