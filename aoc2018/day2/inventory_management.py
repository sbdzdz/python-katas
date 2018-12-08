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

def count_different(s1, s2):
    return sum(int(c1 != c2) for c1, c2 in zip(s1, s2))

def get_common(s1, s2):
    return ''.join(c1 for c1, c2 in zip(s1, s2) if c1 == c2)

def find_correct(ids):
    for i in ids:
        for j in ids:
            if count_different(i, j) == 1:
                return get_common(i, j)

with open('input', 'r') as f:
    ids = f.read().splitlines()

print(calculate_checksum(ids))
print(find_correct(ids))
