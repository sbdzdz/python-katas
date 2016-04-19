def solution(H):
    stack = []
    count = 0
    current = 0
    for height in H:
        if current < height:
            stack.append(height-current)
            current = height
            count += 1
        else:
            while current > height:
                current -= stack.pop()
            if not current == height:
                stack.append(height-current)
                current = height
                count += 1
    return count