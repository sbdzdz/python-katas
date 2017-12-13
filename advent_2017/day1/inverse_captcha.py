def rotate(l, n):
    return l[-n:] + l[:-n]

with open('input', 'r') as f:
    inp = list(f.read().strip())

part_one = sum([int(i) for i, j in zip(inp, rotate(inp, 1)) if i == j])
part_two = sum([int(i) for i, j in zip(inp, rotate(inp, len(inp)//2)) if i == j])

print(part_one, part_two)
