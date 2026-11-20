## Функция для вычисления сумм диагоналей квадратной матрицы
def diagonal_sums(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("Матрица должна быть квадратной")

    sums = []

    # Start on the top row, from the upper-right corner to the left.
    for start_col in range(size - 1, -1, -1):
        sums.append(sum(matrix[i][start_col + i] for i in range(size - start_col)))

    # Then start on the left column below the main diagonal.
    for start_row in range(1, size):
        sums.append(sum(matrix[start_row + offset][offset]
                        for offset in range(size - start_row)))

    return sums

m = int(input("Введите размерность квадратной матрицы: "))
matrix = [list(map(int, input("Введите строку матрицы: ").split())) for _ in range(m)]
print(*diagonal_sums(matrix))