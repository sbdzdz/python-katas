from itertools import islice, cycle, dropwhile

def build_spiral():
    left = left_right()
    up = up_down()
    while True:
        for direction in next(left):
            yield direction
        for direction in next(up):
            yield direction 

def left_right():
    for index, direction in enumerate(cycle('RL')):
        yield direction*(index+1)

def up_down():
    for index, direction in enumerate(cycle('UD')):
        yield direction*(index+1)

def manhattan(position):
    return abs(position[0]) + abs(position[1])

def move(position, direction):
    if direction == 'L':
        return (position[0]-1, position[1])
    if direction == 'R':
        return (position[0]+1, position[1])
    if direction == 'U':
        return (position[0], position[1]+1)
    if direction == 'D':
        return (position[0], position[1]-1)

def are_neighbors(a, b):
    return (abs(a[0]-b[0]) < 2) and (abs(a[1]-b[1]) < 2)

def sum_neighbors(spiral, direction):
    new_element = move(spiral[-1], direction)
    total = sum(element[2] for element in spiral if are_neighbors(element, new_element))
    return (new_element[0], new_element[1], total)

def part_one():
    position = (0, 0)
    for direction in build_spiral():
        yield manhattan(position)
        position = move(position, direction)

def part_two():
    spiral = [(0, 0, 1)]
    for direction in build_spiral():
        new_value = sum_neighbors(spiral, direction)
        spiral.append(new_value)
        yield new_value[2]

inp = 368078
solution_one = list(islice(part_one(), inp))[-1]
solution_two = next(islice(dropwhile(lambda x: x < inp, part_two()), 1))

print(solution_one, solution_two)
