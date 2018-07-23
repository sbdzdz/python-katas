"""
You are given two vectors: `X` and `Y`. Suppose you are allowed to permute the coordinates of each vector as you wish.

Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product. 
"""

def solution(X, Y):
    return sum([x*y for x, y in zip(sorted(X), sorted(Y, reverse=True))])

if __name__=='__main__':
    with open('input', 'r') as infile, open('output', 'w') as out:
        num_testcases = int(next(infile))
        for i in range(num_testcases):
            next(infile)
            X = [int(x) for x in next(infile).split()]
            Y = [int(y) for y in next(infile).split()]
            out.write("Case #{0}: {1}\n".format(i+1, solution(X, Y)))
