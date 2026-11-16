def swap_min_max_columns(matrix):
	if not matrix or not matrix[0]:
		return matrix

	min_value = max_value = matrix[0][0]
	min_col = max_col = 0

	for row in matrix:
		for col, value in enumerate(row):
			if value < min_value:
				min_value = value
				min_col = col
			if value > max_value:
				max_value = value
				max_col = col

	for row in matrix:
		row[min_col], row[max_col] = row[max_col], row[min_col]

	return matrix


if __name__ == "__main__":
	m, n = map(int, input("Введите размерность матрицы: ").split())
	matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(m)]
	swap_min_max_columns(matrix)
	for row in matrix:
		print(*row)
