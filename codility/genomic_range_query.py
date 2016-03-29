def solution(S, P, Q):
    results = []
    prefsum = calculate_prefsum(S)
    for begin, end in zip(P, Q):
        slice = subtract_lists(prefsum[end+1], prefsum[begin])
        results.append(find_minimal_impact(slice))
    return results
    
def find_minimal_impact(slice):
    return next(index+1 for index, element in enumerate(slice) if element)
    
def subtract_lists(list_a, list_b):
    return [a-b for a, b in zip(list_a, list_b)]
    
def calculate_prefsum(S):
    impact = {'A':0, 'C':1, 'G':2, 'T':3}
    length = len(S)
    prefsum = [[0]*4]*(length+1)
    
    for i in range(1, length+1):
        prefsum[i]=list(prefsum[i-1])
        prefsum[i][impact[S[i-1]]] += 1
    return prefsum