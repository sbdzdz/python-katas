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
