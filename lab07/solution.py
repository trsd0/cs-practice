import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    if not values:
        return []
    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return np.round(arr, 6).tolist()


def block(
    matrix: list[list[float]], rows: list[int], columns: list[int]
) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    sub = arr[np.ix_(rows, columns)]
    return np.round(sub, 6).tolist()
