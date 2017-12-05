import inputs

def rotate(l, n):
    return l[-n:] + l[:-n]

input = list(inputs.captcha)
part_one = sum([int(i) for i, j in zip(input, rotate(input, 1)) if i == j])
part_two = sum([int(i) for i, j in zip(input, rotate(input, len(input)//2)) if i == j])

print(part_one, part_two)
