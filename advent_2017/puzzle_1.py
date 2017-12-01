import inputs

def rotate(l, n):
    return l[-n:] + l[:-n]

input = list(puzzle_1)
print(sum([int(i) for i, j in zip(input, rotate(input, 1)) if i == j]))
print(sum([int(i) for i, j in zip(input, rotate(input, len(input)//2)) if i == j]))
