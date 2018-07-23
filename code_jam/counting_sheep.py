"""
Bleatrix "Trotter" the sheep has devised a strategy that helps her fall asleep faster. 

First, she picks a number `N`. Then she starts naming `N`, `2N`, `3N`, and so on.
She keeps track of which digits she has seen at least once so far as part of any number she has named. 
Once she has seen each of the ten digits at least once, she will fall asleep. 

Knowing `N`, print the last number Bleatrix will see before falling asleep. If the poor sheep will count forever, print INSOMNIA instead.
"""

def solution(N):
    if N == 0:
        return 'INSOMNIA'
    else:
        digits = set(range(10))
        seen = set() 
        current = 0
        while seen != digits:
            current += N
            for digit in str(current):
                seen.add(digit)
        return current

with open('input.in', 'r') as infile, open('output', 'w') as out:
    next(infile)
    for index, line in enumerate(infile):
        N = int(line)
        out.write("Case #{0}: {1}\n".format(index+1, solution(N)))
