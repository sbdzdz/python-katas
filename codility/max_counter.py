"""
You are given N counters and a non empty array A of M integers
representing a sequence of operations:

- if A[K]=X such that 1 <= X <= N, increment counter X
- if A[K]=N+1, set all counters to the value of the maximal counter

Calculate the value of every counter after all operations.
"""

def solution(N, A):
    counters = [0]*N
    last_max_counter = 0
    max_counter = 0
    for index in A:
        if index <= N:
            if counters[index-1] < last_max_counter:
                counters[index-1] = last_max_counter
            counters[index-1] += 1
            max_counter = max(max_counter, counters[index-1])
        else:
            last_max_counter = max_counter
    return [max(last_max_counter, counter) for counter in counters]
