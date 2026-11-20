# Дано целое число m и натуральное число n. Найти номер столбца, все элементы которого являются нечетными числами.
def find_column_all_odd(matrix):

    if not matrix or not matrix[0]:
        return -1
    
    m = len(matrix)      
    n = len(matrix[0])   
    
    for col in range(n):
        all_odd = True
        for row in range(m):
            if matrix[row][col] % 2 == 0: 
                all_odd = False
                break
        if all_odd:
            return col + 1
    
    return -1 


if __name__ == "__main__":
    try:
        m, n = map(int, input("Введите размерность матрицы (m n): ").split())
        print("Введите элементы матрицы построчно:")
        matrix = [list(map(int, input(f"Строка {i+1}: ").split())) for i in range(m)]
        
        # Проверка корректности ввода
        for i, row in enumerate(matrix):
            if len(row) != n:
                print(f"Ошибка: в строке {i+1} должно быть {n} элементов")
                exit()
        
        result = find_column_all_odd(matrix)
        
        if result != -1:
            print(f"Номер столбца, все элементы которого нечетные: {result}")
        else:
            print("Нет столбца, все элементы которого являются нечетными числами")
            
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целые числа.")
