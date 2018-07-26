def fibonacci_recursive(n):
    if n < 2:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n < 2:
        return 1
    else:
        previous = 1
        current = 1
        for i in range(n-1):
            total = previous + current
            previous = current
            current = total 
    return current
