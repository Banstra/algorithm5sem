# Функция для подсчета элементов в каждом столбце, превышающих среднее значение столбца
def count_above_column_average(matrix):

	if not matrix:
		return []

	column_count = len(matrix[0])
	if any(len(row) != column_count for row in matrix):
		raise ValueError("Все строки матрицы должны иметь одинаковую длину.")

	result = []
	for column in range(column_count):
		values = [row[column] for row in matrix]
		average = sum(values) / len(values)
		result.append(sum(value > average for value in values))
	return result



rows, columns = map(int, input("Введите размерность матрицы: ").split())
matrix = [list(map(float, input("Введите строку матрицы: ").split())) for _ in range(rows)]
print(*count_above_column_average(matrix))
