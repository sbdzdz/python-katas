from functools import reduce
from operator import xor

def generate_sparse_hash(lengths, num_iter=1):
    string = list(range(256))
    skip = 0
    pos = 0
    for _ in range(num_iter):
        for length in lengths:
            string = twist(string, pos, length)
            pos = (pos+skip+length)%len(string)
            skip += 1
    return string

def twist(string, position, length):
    first = slice(position, position+length)
    second = slice(None, max(0, position+length-len(string)))
    twisted = list(reversed(string[first]+string[second]))

    len_first = len(string[first])
    string[first] = twisted[:len_first]
    string[second] = twisted[len_first:]
    return string

def to_dense(hsh):
    return [reduce(xor, s) for s in chunks(hsh, 16)]

def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]

def generate_hash(text, num_iter=1):
    inp = [ord(c) for c in text] + [17, 31, 73, 47, 23]
    sparse = generate_sparse_hash(inp, 64)
    dense = to_dense(sparse)
    return to_bin(dense)

def to_bin(hsh):
    hex_str = ''.join(format(c, '02x') for c in hsh)
    bin_str = ''.join(format(int(c, 16), '04b') for c in hex_str)
    bin_int = [int(c) for c in bin_str]
    return bin_int 

def generate_grid(base):
    grid = []
    for suffix in range(128):
        name = '{}-{}'.format(base, suffix)
        grid.append(generate_hash(name))
    return grid

def get_adjacent(length, coord):
    adjacent = []
    x, y = coord
    for node in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
        if 0 <= node[0] < length and 0 <= node[1] < length:
            adjacent.append(node)
    return adjacent

def mark_group(grid, coord):
    group = [coord]
    while group:
        node = group.pop()
        for x, y in get_adjacent(len(grid), node):
            if grid[x][y]:
                group.append((x, y))
                grid[x][y] = 0

def count_groups(grid):
    num_groups = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value:
                num_groups += 1
                mark_group(grid, (x, y))
    return num_groups

if __name__ == '__main__':
    base = 'hxtvlmkl'
    grid = generate_grid(base)
    print(sum(sum(line) for line in grid))
    print(count_groups(grid))
