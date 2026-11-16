
n = int(input("Введите количество элементов массива: "))
array = list(map(float, input("Введите элементы через пробел: ").split()))
k, l = map(int, input("Введите k и l через пробел: ").split())
print(sum(array[k - 1:l]) / (l - k + 1))

