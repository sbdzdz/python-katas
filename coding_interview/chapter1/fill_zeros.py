import numpy as np


def fill_zeros(arr):
    if not arr:
        return arr
    zero_rows = set()
    zero_cols = set()
    m = len(arr)
    n = len(arr[0])

    for i, row in enumerate(arr):
        for j, element in enumerate(row):
            if arr[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for row in zero_rows:
        arr[row] = [0] * n
    for col in zero_cols:
        for row in arr:
            row[col] = 0
    return arr


def fill_zeros_pythonic(arr):
    arr = np.array(arr)
    rows, cols = np.where(arr == 0)
    for row, col in zip(rows, cols):
        arr[row, :] = 0
        arr[:, col] = 0
    return arr.tolist()
