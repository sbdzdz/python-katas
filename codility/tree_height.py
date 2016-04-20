def solution(T):
    if not T:
        return -1
    fringe = [(T, 0)]
    while fringe:
        current, depth = fringe.pop(0)
        if current.l:
            fringe.append((current.l, depth+1))
        if current.r:
            fringe.append((current.r, depth+1))
    return depth