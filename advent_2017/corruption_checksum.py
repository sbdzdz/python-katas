import inputs

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

input = inputs.checksum.split('\n')
checksum1 = sum(min_max(parse(line)) for line in input)
checksum2 = sum(divisor(parse(line)) for line in input)
print(checksum1, checksum2)
