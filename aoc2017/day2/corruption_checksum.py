def parse(line):
    return [int(n) for n in line.split()]

def min_max(line):
    return max(line) - min(line)

def divisor(line):
    line.sort()
    for index, divisor in enumerate(line):
        for multiple in line[index+1:]:
            if multiple%divisor == 0:
                return multiple // divisor

with open('input') as f:
    inp = f.readlines()

part_one = sum(min_max(parse(line)) for line in inp)
part_two = sum(divisor(parse(line)) for line in inp)

print(part_one, part_two)
