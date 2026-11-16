def swap_row_min_max(matrix):
	for row in matrix:
		if not row:
			continue
		min_index = row.index(min(row))
		max_index = row.index(max(row))
		row[min_index], row[max_index] = row[max_index], row[min_index]
	return matrix


if __name__ == "__main__":
	m, n = map(int, input("Введите размерность матрицы: ").split())
	matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(m)]

	swap_row_min_max(matrix)

	for row in matrix:
		print(*row)
