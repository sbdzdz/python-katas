def solution(A):
    total = 0
    prefsum = calculate_prefsum(A)
    for index, element in enumerate(A):
        if element == 0:
            total += prefsum[-1]-prefsum[index]
            if total > 1000000000:
                return -1
    return total

def calculate_prefsum(A):
    n = len(A)
    prefsum = [0]*(n+1)
    for i in xrange(1, n+1):
        prefsum[i] = prefsum[i-1]+A[i-1]
    return prefsum
