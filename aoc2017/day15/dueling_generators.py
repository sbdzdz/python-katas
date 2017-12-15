class Generator():
    def __init__(self, start, factor):
        self.previous = start
        self.factor = factor
        self.divisor = 2147483647

    def __iter__(self):
        return(self)

    def __next__(self):
        current = (self.previous*self.factor)%self.divisor
        self.previous = current
        return current

def match(a, b):
    xor = format(a^b, '32b')[-16:]
    return not int(xor)

def generator_a():
    while True:
        current = previous*factor%divisor

num_iter = 40000000

a = Generator(65, 16807)
b = Generator(8921, 48271)

print(sum(match(next(a), next(b)) for _ in range(num_iter)))
