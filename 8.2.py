
def swap_min_max(matrix):
    """
    Находит наибольший и наименьший элементы в прямоугольной матрице
    и меняет их местами.

    Args:
        matrix: Двумерный массив (матрица).

    Returns:
        Измененная матрица с поменянными местами максимальным и минимальным элементами.
        Возвращает исходную матрицу, если она пуста.
    """
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    matrix = np.array(matrix) # Преобразуем в NumPy array для удобства

    # Находим индексы максимального и минимального элементов
    max_index = np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)
    min_index = np.unravel_index(np.argmin(matrix, axis=None), matrix.shape)

    # Меняем элементы местами
    matrix[max_index], matrix[min_index] = matrix[min_index], matrix[max_index]

    return matrix.tolist() # Возвращаем в виде списка списков

# Пример использования:
matrix = [
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 9]
]

modified_matrix = swap_min_max(matrix)
print(f"Исходная матрица:\n{np.array(matrix)}")
print(f"Измененная матрица:\n{np.array(modified_matrix)}")


# Дополнительные примеры:
matrix2 = [[10, 2], [3, 40]]
modified_matrix2 = swap_min_max(matrix2)
print(f"Исходная матрица:\n{np.array(matrix2)}")
print(f"Измененная матрица:\n{np.array(modified_matrix2)}")

matrix3 = [[5]]  # Матрица 1x1
modified_matrix3 = swap_min_max(matrix3)
print(f"Исходная матрица:\n{np.array(matrix3)}")
print(f"Измененная матрица:\n{np.array(modified_matrix3)}")

matrix4 = [] #Пустая матрица
modified_matrix4 = swap_min_max(matrix4)
print(f"Исходная матрица:\n{np.array(matrix4)}")
print(f"Измененная матрица:\n{np.array(modified_matrix4)}")