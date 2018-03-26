import copy

def rotate_array(arr):
    arr_rotated = copy.deepcopy(arr)
    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            arr_rotated[j][len(arr)-1-i] = element
    return arr_rotated

def rotate_array_in_place(arr):
    n = len(arr)
    if n == 1:
        return arr
    for ring in range((n+1)//2):
        for i in range(ring, n-ring-1):
            arr[ring][i], arr[i][n-1-ring], arr[n-1-ring][n-1-i], arr[n-1-i][ring] = \
            arr[n-1-i][ring], arr[ring][i], arr[i][n-1-ring], arr[n-1-ring][n-1-i]
    return arr
