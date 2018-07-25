"""
Find the minimal perimeter of a rectangle whose area equals N.

Assume that the lengths of sides are integers.
"""

def solution(N):
    perimeters = []
    counter = 1
    while counter**2 <= N:
        if N%counter==0:
            perimeters.append(calculate_perimeter(counter, N/counter))
        counter += 1
    return min(perimeters)
    
def calculate_perimeter(a, b):
    return 2*(a+b)
