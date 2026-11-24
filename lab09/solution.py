import numpy as np


# Задание 1
def make_hours() -> list[int]:
    return np.arange(0, 22, 3, dtype=int).tolist()


# Задание 2
def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }


# Задание 3
def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()


# Задание 4
def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[arr > limit] = limit
    return arr.tolist()


# Задание 5
def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float)
    fahrenheit = arr * 9 / 5 + 32
    return fahrenheit.tolist()
