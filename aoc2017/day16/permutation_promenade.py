from string import ascii_lowercase
from itertools import count

def spin(programs, n):
    return programs[-n:] + programs[:len(programs)-n]

def exchange(programs, a, b):
    programs = list(programs)
    programs[a], programs[b] = programs[b], programs[a]
    return ''.join(programs)

def partner(programs, a, b):
    mapping = str.maketrans(a+b, b+a)
    return programs.translate(mapping)

def dance(programs, choreography):
    for command in choreography.split(','):
        if command.startswith('s'):
            n = int(command[1:])
            programs = spin(programs, n)

        if command.startswith('x'):
            a, b = command[1:].split('/')
            programs = exchange(programs, int(a), int(b))

        if command.startswith('p'):
            a, b = command[1:].split('/')
            programs = partner(programs, a, b)
    return programs

def find_period(programs, choreography):
    init_perm = programs
    for i in count(1):
        programs = dance(programs, choreography)
        if programs == init_perm:
            return i

if __name__ == '__main__':
    with open('input') as f:
        inp = f.read()
    programs = ascii_lowercase[:16]

    repeats_after = find_period(programs, inp)
    num_iter = int(1e9)%repeats_after

    solution_one = dance(programs, inp)
    for _ in range(num_iter):
        programs = dance(programs, inp)
    solution_two = programs

    print(solution_one, solution_two)
