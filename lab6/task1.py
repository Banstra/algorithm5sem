# Функция для обхода матрицы по спирали против часовой стрелки
def spiral_counterclockwise(matrix):
	n = len(matrix)
	result = []

	for layer in range((n + 1) // 2):
		edge = n - 1 - layer

		# Первый столбец слоя, сверху вниз.
		for row in range(layer, edge + 1):
			result.append(matrix[row][layer])

		# Последняя строка, слева направо.
		for col in range(layer + 1, edge + 1):
			result.append(matrix[edge][col])

		if edge > layer:
			# Последний столбец, снизу вверх.
			for row in range(edge - 1, layer - 1, -1):
				result.append(matrix[row][edge])

			# Первая строка, справа налево.
			for col in range(edge - 1, layer, -1):
				result.append(matrix[layer][col])

	return result


n = int(input("Введите размерность матрицы: "))
matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(n)]
print(*spiral_counterclockwise(matrix))
