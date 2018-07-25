from stack import Stack

def sort_stack(stack):
    ordered = Stack()
    while not stack.is_empty():
        current = stack.pop()
        while not ordered.is_empty() and current < ordered.peek():
            stack.push(ordered.pop())
        ordered.push(current)
    return ordered
