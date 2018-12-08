def dist_from_max(index, max_index, length):
    if index > max_index:
        return index - max_index
    else:
        return length-max_index + index

def update(memory):
    max_value = max(memory)
    max_index = memory.index(max_value)
    memory[max_index] = 0
    for index, element in enumerate(memory):
        memory[index] += max_value // len(memory)
        if dist_from_max(index, max_index, len(memory)) <= max_value % len(memory):
            memory[index] += 1

def solve(memory):
    states = dict()
    while tuple(memory) not in states:
        states[tuple(memory)] = len(states)
        update(memory)
    return len(states), len(states)-states[tuple(memory)]

with open('input') as f:
    memory_banks = [int(e) for e in f.read().split()]

part_one, part_two = solve(memory_banks)

print(part_one, part_two)

