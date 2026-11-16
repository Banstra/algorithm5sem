n = int(input("Введите количество нечетных чисел: "))
total = 0

for odd in range(1, 2 * n, 2):
    total += odd
    print(f"Сумма первых {n} нечетных чисел: {total}")