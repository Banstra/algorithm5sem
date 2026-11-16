def sort_rows_by_first_element(matrix):
    return sorted(matrix, key=lambda row: row[0])


rows, columns = map(int, input("Введите размерность матрицы: ").split())
matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(rows)]

if any(len(row) != columns for row in matrix):
    raise ValueError("Каждая строка матрицы должна содержать одинаковое количество элементов")

for row in sort_rows_by_first_element(matrix):
    print(*row)
