def insertion_sort_with_steps(arr):

    print(f"Начальный массив: {arr}\n")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Шаг {i}: вставляем элемент {key}")
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"  После вставки: {arr}\n")
    
    return arr

my_list = input("Введите список чисел через пробел: ").split()
my_list = [int(x) for x in my_list]
insertion_sort_with_steps(my_list)