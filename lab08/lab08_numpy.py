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

# Задание 4.
matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
first_three_rows = matrix[:3]
print("Первые три строки:\n", first_three_rows, "shape:", first_three_rows.shape)

last_two_rows = matrix[-2:]
print("Последние две строки:\n", last_two_rows, "shape:", last_two_rows.shape)

first_two_cols = matrix[:, :2]
print("Первые два столбца:\n", first_two_cols, "shape:", first_two_cols.shape)

middle_block = matrix[1:4, 2:5]
print("Строки 1–3, столбцы 2–4:\n", middle_block, "shape:", middle_block.shape)

bottom_right = matrix[-2:, -2:]
print("Правый нижний блок 2x2:\n", bottom_right, "shape:", bottom_right.shape)

# Задание 5.
print("\nЗадание 5")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)
# Метод .copy() нужен для создания дубликата данных в памяти
# Без .copy() изменения затронули бы и исходный массив hours


changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:\n", changed_matrix)
print("Исходная matrix:\n", matrix)

# Задание 6.
print("\n--- Задание 6 ---")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers shape:", numbers.shape)
print("table shape:", table.shape)
print("transposed shape:", transposed.shape)
# reshape(3, 4) работает, потому что в массиве numbers 12 элементов (3x4 = 12)
# reshape(5, 3) вызовет ошибку ValueError, ибо в массиве numbers 12 элементов, а 5x3 = 15
