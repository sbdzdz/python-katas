from itertools import cycle

def find_resulting_frequency(shifts):
    return sum(shifts)

def find_duplicate_frequency(shifts):
    seen = set([0]) 
    frequency = 0
    for shift in cycle(shifts):
        frequency += shift
        if frequency in seen:
            return frequency
        seen.add(frequency)

with open('input', 'r') as f:
    shifts = [int(line) for line in f]

print(find_resulting_frequency(shifts))
print(find_duplicate_frequency(shifts))
