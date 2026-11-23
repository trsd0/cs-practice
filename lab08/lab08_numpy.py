import numpy as np

# Задание 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print(
    "shape:",
    hours.shape,
    "ndim:",
    hours.ndim,
    "size:",
    hours.size,
    "dtype:",
    hours.dtype,
)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

# Задание 2
print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

# Задание 3. Строки и столбцы таблицы
temperatures = np.array(
    [
        [12, 14, 13, 15],
        [11, 13, 16, 17],
        [10, 12, 15, 18],
    ]
)

print("\nЗадание 3")
print(
    "shape:", temperatures.shape, "ndim:", temperatures.ndim, "size:", temperatures.size
)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
central = temperatures[:2, 1:3]
print("Центральный фрагмент 2x2 (shape =", central.shape, "):\n", central)
