
rows, columns = map(int, input("Введите размерность матрицы: ").split())
matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(rows)]

products = [1] * columns
for row in matrix:
	for column, value in enumerate(row):
		products[column] *= value

minimum_index = min(range(columns), key=products.__getitem__)
print("Номер столбца с наименьшим произведением:", minimum_index + 1)
print("Наименьшее произведение:", products[minimum_index])

