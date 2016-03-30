def solution(X, A):
    required = set(range(1, X+1))
    for index, element in enumerate(A):
        if element in required:
            required.remove(element)
        if not required:
            return index
    return -1