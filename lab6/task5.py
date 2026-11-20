# Дано целое число m и натуральное число n. Найти номер столбца, все элементы которого являются нечетными числами.
def main():
	m, n = map(int, input("Введите размерность матрицы: ").split())
	matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(m)]

	for column in range(n):
		if all(matrix[row][column] % 2 != 0 for row in range(m)):
			print(column + 1)
			return

	print(0)


if __name__ == "__main__":
	main()
