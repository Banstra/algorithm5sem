
n = int(input("Введите количество элементов массива: "))
a = list(map(int, input("Введите элементы через пробел: ").split()))
print(min(a[1:n:2]))

