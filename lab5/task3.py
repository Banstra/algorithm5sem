n = int(input("Введите количество элементов массива: "))
a, b = map(int, input("Введите первые два элемента через пробел: ").split())

array = [a, b]
for _ in range(2, n):
    array.append(sum(array))

print(*array)