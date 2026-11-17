def bubble_sort(arr):
    n = len(arr) 
    for i in range(n):
        print("шаг", i + 1, ":", arr)
        swapped = False 
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True       
        if not swapped:
            break      
    return arr


my_list = input("Введите список чисел через пробел: ").split()
my_list = [int(x) for x in my_list]

print("Исходный список:", my_list)

sorted_list = bubble_sort(my_list)

print("Отсортированный список:", sorted_list)