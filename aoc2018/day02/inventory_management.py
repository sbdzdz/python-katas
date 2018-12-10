from collections import Counter

def calculate_checksum(ids):
    two = 0
    three = 0
    for i in ids:
        counts = Counter(i)
        if 2 in counts.values():
            two += 1
        if 3 in counts.values():
            three += 1
    return two * three

def find_correct(ids):
    seen  = set()
    for i in ids:
        for j in range(len(i)):
            substring = i[:j] + '_' + i[j+1:]
            if substring in seen:
                return substring.replace('_', '')
            seen.add(substring)

with open('input', 'r') as f:
    ids = f.read().splitlines()

print(calculate_checksum(ids))
print(find_correct(ids))