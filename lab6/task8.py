# Функция для обмена местами четвертей матрицы
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
    
    # Меняем местами все четыре четверти по диагонали
    for i in range(half_rows):
        for j in range(half_columns):
            # Верхняя левая - Нижняя правая
            matrix[i][j], matrix[i + half_rows][j + half_columns] = (
                matrix[i + half_rows][j + half_columns], matrix[i][j]
            )
            # Верхняя правая - Нижняя левая
            matrix[i][j + half_columns], matrix[i + half_rows][j] = (
                matrix[i + half_rows][j], matrix[i][j + half_columns]
            )
    
    return matrix


if __name__ == "__main__":
    try:
        rows, columns = map(int, input("Введите размерность матрицы (rows columns): ").split())
        print("Введите элементы матрицы построчно:")
        matrix = [list(map(int, input(f"Строка {i+1}: ").split())) for i in range(rows)]
        
        # Проверка корректности ввода
        for i, row in enumerate(matrix):
            if len(row) != columns:
                print(f"Ошибка: в строке {i+1} должно быть {columns} элементов")
                exit()
        
        swap_quarters(matrix)
        
        print("\nМатрица после обмена четвертей:")
        for row in matrix:
            print(*row)
            
    except ValueError as e:
        print(f"Ошибка: {e}")