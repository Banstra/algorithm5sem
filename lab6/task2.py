
m, n = map(int, input("Введите размерность матрицы: ").split())
matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(m)]
k = int(input("Введите номер строки: "))

row = matrix[k - 1]
total = sum(row)
product = 1
for value in row:
	product *= value
print("Всего:", total, "Произведение:", product)

