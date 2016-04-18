def solution(A):
    discs = []
    count = 0
    open_discs = 0
    for center, radius in enumerate(A):
        discs.append((center-radius, -1))
        discs.append((center+radius, 1))
    discs = [disc[1] for disc in sorted(discs)]
    for element in discs:
        if element == -1:
            count -= open_discs
        open_discs += element
    return count if count <= 10**7 else -1