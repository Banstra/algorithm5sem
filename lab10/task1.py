def binary_search_with_steps(arr, target):

    left = 0
    right = len(arr) - 1
    step = 1
    
    print(f"Ищем элемент {target} в массиве {arr}\n")
    
    while left <= right:
        mid = left + (right - left) // 2
        
        print(f"Шаг {step}:")
        print(f"  Диапазон: [{left}, {right}]")
        print(f"  Средний индекс: {mid}")
        print(f"  Средний элемент: {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  ✓ Найдено! Элемент {target} находится по индексу {mid}")
            return mid
        elif arr[mid] < target:
            print(f"  → {arr[mid]} < {target}, сдвигаем левую границу вправо")
            left = mid + 1
        else:
            print(f"  ← {arr[mid]} > {target}, сдвигаем правую границу влево")
            right = mid - 1
        
        step += 1
        print()
    
    print(f"✗ Элемент {target} не найден")
    return -1


my_list = [int(x) for x in input("Введите список чисел через пробел: ").split()]
search_target = int(input("Введите число для поиска: "))

binary_search_with_steps(my_list, search_target)