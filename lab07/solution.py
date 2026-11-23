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


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix or not matrix[0]:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)
    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix or not matrix[0]:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col = arr[:, column]
    diff = float(np.max(col) - np.min(col))
    return np.round(diff, 6)
