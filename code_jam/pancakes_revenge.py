def counter(function):
    def wrapper(*args):
        wrapper.called += 1
        return function(*args)
    wrapper.called = 0
    wrapper.__name__ = function.__name__
    return wrapper

@counter
def flip(stack, index):
    left, right = stack[:index+1], stack[index+1:]
    return invert(left[::-1]) + right

def invert(stack):
    return stack.replace('-', '%temp%').replace('+', '-').replace('%temp%', '+')

def solution(stack):
    flip.called = 0
    while '-' in stack:
        first_unhappy = stack.find('-')
        if first_unhappy > 0:
            stack = flip(stack, first_unhappy-1)
        stack = flip(stack, stack.rfind('-'))
    return flip.called

with open('input', 'r') as infile, open('output', 'w') as out:
    next(infile)
    for index, line in enumerate(infile):
        out.write("Case #{0}: {1}\n".format(index+1, solution(line)))
