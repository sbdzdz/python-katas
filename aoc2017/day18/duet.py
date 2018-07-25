from collections import defaultdict

with open('input') as f:
    call = {'set': lambda reg,x,y: reg.__setitem__(x, y),
            'add': lambda reg,x,y: reg.__setitem__(x, reg.get(x, 0) + y),
            'mul': lambda reg,x,y: reg.__setitem__(x, reg.get(x, 0) * y),
            'mod': lambda reg,x,y: reg.__setitem__(x, reg.get(x, 0) % y)}

def build_parser(registers):
    def parse(arg):
        if str.isalpha(arg):
            return registers.get(arg, 0)
        else:
            return int(arg)
    return parse

def solve(instructions):
    registers = dict() 
    parse = build_parser(registers)
    index = 0
    while index >= 0 and index < len(instructions):
        current = instructions[index]
        print(current)
        if current.startswith('snd'):
            last_played = parse(current.split()[1])
        elif current.startswith('jgz'):
            _, x, y = current.split()
            if parse(x) > 0:
                index += parse(y)
                continue
        elif current.startswith('rcv'):
            _, x = current.split()
            if parse(x) != 0:
                return last_played
        else:
            function, x, y = current.split()
            y = parse(y)
            call[function](registers, x, y)
        index += 1
        print(registers)

if __name__ == '__main__':
    reg = dict()
    with open('input') as f:
        instructions = f.readlines()
    print(solve(instructions))
