## Дано целое число N, а также массив из N действительных чисел. Найти номер последнего максимального элемента массива.
n = int(input("Введите количество элементов массива: "))
array = list(map(int, input("Введите элементы через пробел: ").split()))

last_maximum = 0
for i, value in enumerate(array):
    greater_than_left = i == 0 or value > array[i - 1]
    greater_than_right = i == n - 1 or value > array[i + 1]
    if greater_than_left and greater_than_right:
        last_maximum = i + 1

print(last_maximum)
