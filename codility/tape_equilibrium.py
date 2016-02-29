def solution(A):
    differences = []
    left = 0
    right = sum(A)
    for element in A[:-1]:
        left += element
        right -= element
        differences.append(abs(left - right))
    return min(differences)
