
def find_min_in_even_rows(matrix):
  """
  Находит наименьший элемент в каждой четной строке матрицы.

  Args:
    matrix: Двумерный массив (матрица).

  Returns:
    Список, содержащий наименьшие элементы каждой четной строки.
    Возвращает пустой список, если матрица пустая или не содержит четных строк.
  """
  if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
    return []

  min_elements = []
  for i in range(0, len(matrix), 2):  # Перебираем только четные строки (индексы 0, 2, 4 и т.д.)
    min_elements.append(min(matrix[i]))

  return min_elements

# Пример использования:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

min_values = find_min_in_even_rows(matrix)
print(f"Матрица:\n{np.array(matrix)}")  # Выводим матрицу для наглядности, используя NumPy
print(f"Минимальные элементы четных строк: {min_values}")

# Пример использования с NumPy array:
matrix_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
min_values_np = find_min_in_even_rows(matrix_np.tolist()) #Преобразуем в список списков
print(f"NumPy матрица:\n{matrix_np}")
print(f"Минимальные элементы четных строк (NumPy): {min_values_np}")

# Пример с пустой матрицей
empty_matrix = []
print(f"Минимальные элементы четных строк пустой матрицы: {find_min_in_even_rows(empty_matrix)}")

# Пример с матрицей, не содержащей четных строк
matrix_odd_rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
min_values_odd_rows = find_min_in_even_rows(matrix_odd_rows)
print(f"Минимальные элементы четных строк матрицы с нечетным количеством строк: {min_values_odd_rows}")