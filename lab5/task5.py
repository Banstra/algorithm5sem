## Дано целое число N, а также массив из N действительных чисел. Переставить элементы массива так, чтобы сначала шли элементы с четными индексами в порядке возрастания, а затем элементы с нечетными индексами в порядке убывания.
def rearrange_compact(arr):

    part1 = sorted(arr[::2])

    part2 = sorted(arr[1::2], reverse=True)
    return part1 + part2

try:
    n_input = input("Введите количество элементов N: ")
    if not n_input.isdigit():
        raise ValueError("N должно быть целым числом")
    n = int(n_input)
    
    print(f"Введите {n} действительных чисел через пробел:")
    arr_input = input().split()
    
    if len(arr_input) != n:
        raise ValueError(f"Количество введенных чисел не совпадает с N ({n})")
        
    # Преобразуем в float (действительные числа)
    original_array = [float(x) for x in arr_input]
    
    # Выполняем перестановку
    new_array = rearrange_compact(original_array)
    
    # Вывод результата
    print("\nИсходный массив:", original_array)
    print("Результат:", new_array)
    
    # Для наглядности покажем, какие элементы куда попали
    print("\n--- Детализация ---")
    evens = [original_array[i] for i in range(0, n, 2)]
    odds = [original_array[i] for i in range(1, n, 2)]
    print(f"Элементы с четных индексов (до сортировки): {evens}")
    print(f"Элементы с нечетных индексов (до сортировки): {odds}")
    print(f"Четные индексы (отсортированы возр.): {sorted(evens)}")
    print(f"Нечетные индексы (отсортированы убыв.): {sorted(odds, reverse=True)}")

except ValueError as e:
    print(f"Ошибка ввода: {e}")
