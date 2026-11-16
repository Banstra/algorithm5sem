def swap_quarters(matrix):
	rows = len(matrix)
	if rows == 0:
		return matrix

	columns = len(matrix[0])
	if rows % 2 or columns % 2:
		raise ValueError("матрица должна иметь четное количество строк и столбцов")
	if any(len(row) != columns for row in matrix):
		raise ValueError("матрица должна быть прямоугольной")

	half_rows, half_columns = rows // 2, columns // 2
	for i in range(half_rows):
		for j in range(half_columns):
			matrix[i][j], matrix[i + half_rows][j + half_columns] = (
				matrix[i + half_rows][j + half_columns], matrix[i][j]
			)
	return matrix


rows, columns = map(int, input("Введите размерность матрицы: ").split())
matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(rows)]
swap_quarters(matrix)
for row in matrix:
	print(*row)

