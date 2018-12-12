import re
from collections import defaultdict

def make_claims(claims):
    fabric = defaultdict(int)
    for claim in claims:
        _, x, y, w, h = claim
        x, y, w, h = int(x), int(y), int(w), int(h)
        for i in range(x, x+w):
            for j in range(y, y+h):
                fabric[(i, j)] += 1
    return fabric

def count_overlaps(fabric):
    return len([p for p in fabric if fabric[p] > 1])

def find_intact_claim(fabric, claims):
    for claim in claims:
        point_values = []
        claim_id, x, y, w, h = claim
        x, y, w, h = int(x), int(y), int(w), int(h)
        if all(fabric[i, j] == 1 for i in range(x, x+w) for j in range(y, y+h)):
            return claim_id

with open('input') as f:
    p = re.compile(r'\#(\d+)\ @\ (\d+),(\d+)\:\ (\d+)x(\d+)')
    claims = []
    for line in f:
        claims.append(p.match(line).groups())

fabric = make_claims(claims)
print(count_overlaps(fabric))
print(find_intact_claim(fabric, claims))
