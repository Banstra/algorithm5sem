def selection_sort_with_steps(arr):
    n = len(arr)
    print(f"Начальный массив: {arr}\n")
    
    for i in range(n - 1):
        min_idx = i
        print(f"Шаг {i + 1}: ищем минимум в неотсортированной части {arr[i:]}")
        print(f"  Предполагаемый минимум: {arr[i]} (индекс {i})")
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"  Найден меньший элемент: {arr[j]} (индекс {j})")
        
        if min_idx != i:
            print(f"  Меняем местами: {arr[i]} <-> {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"  Элемент уже на своем месте")
        
        print(f"  Результат: {arr}\n")
    
    return arr


my_list = input("Введите список чисел через пробел: ").split()
my_list = [int(x) for x in my_list]
selection_sort_with_steps(my_list)