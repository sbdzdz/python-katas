def match(a, b):
    xor = format(a^b, '32b')[-16:]
    return not int(xor)

def gen(start, factor):
    while True:
        start = (start * factor) % 2147483647
        yield start

def solve_first():
    a = gen(618, 16807)
    b = gen(814, 48271)

    num_iter = 40000000
    return sum(match(next(a), next(b)) for _ in range(num_iter))

def solve_second():
    num_iter = 5000000
    gen_a = (a for a in gen(618, 16807) if a % 4 == 0)
    gen_b = (b for b in gen(618, 16807) if b % 8 == 0)
    return sum(match(next(gen_a), next(gen_b)) for _ in range(num_iter))


if __name__ == '__main__':
    print(solve_first())
    print(solve_second())
