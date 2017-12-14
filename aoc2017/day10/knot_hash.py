import operator
import functools

def generate_sparse_hash(lengths, iterations=1):
    string = list(range(256))
    skip = 0
    pos = 0
    for _ in range(iterations):
        for length in lengths:
            string = twist(string, pos, length)
            pos = (pos+skip+length)%len(string)
            skip += 1
    return string

def twist(string, position, length):
    first = slice(position, position+length)
    second = slice(None, max(0, position+length-len(string)))
    to_reverse = string[first]+string[second]
    len_first = len(string[first])
    string[first] = list(reversed(to_reverse))[:len_first]
    string[second] = list(reversed(to_reverse))[len_first:]
    return string

def to_dense(hsh):
    return [xor_fold(s) for s in chunks(hsh, 16)]

def xor_fold(seq):
    return functools.reduce(operator.xor, seq) 

def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]

def to_hex(seq):
    return ''.join(format(c, '02x') for c in seq)

if __name__ == '__main__':
    with open('input') as f:
        inp = f.read().strip()

    lengths1 = [int(i) for i in inp.split(',')]
    lengths2 = [ord(c) for c in inp] + [17, 31, 73, 47, 23]

    hash1 = generate_sparse_hash(lengths1)
    hash2 = generate_sparse_hash(lengths2, 64)

    print(hash1[0]*hash1[1])
    print(to_hex(to_dense(hash2)))
