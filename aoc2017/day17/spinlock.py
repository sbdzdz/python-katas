def solve_first(step):
    buff = [0]
    position = 0
    for value in range(1, 2018):
        position = (position + 1 + step) % len(buff)
        buff = buff[:position+1] + [value] + buff[position+1:]
    return buff[buff.index(2017)+1]

def solve_second(step, n):
    position = 0
    length = 1
    after_zero = 0
    for value in range(1, n):
        position = (position + 1 + step) % length
        if position == 0:
            after_zero = value
        length += 1
    return after_zero

if __name__ == '__main__':
    inp = 380
    n = 50000000
    print(solve_first(inp))
    print(solve_second(inp, n))
