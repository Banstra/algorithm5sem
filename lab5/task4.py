# Дано целое число N, а также массив из N целых чисел. Переставить элементы массива в обратном порядке (первый элемент становится последним, второй — предпоследним и т.д.).
def reverse_array_slicing(arr):

    return arr[::-1]

n = int(input("Введите количество элементов N: "))
print(f"Введите {n} целых чисел через пробел:")
array = list(map(int, input().split()))

if len(array) != n:
    print(f"Ошибка: введено {len(array)} чисел вместо {n}")
else:
    reversed_array = reverse_array_slicing(array)
    print("Исходный массив:", array)
    print("Перевернутый массив:", reversed_array)
