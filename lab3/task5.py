A = float(input("Введите число A: "))
N = int(input("Введите число N: "))

result = 1.0
power = 1.0
sign = -1

for _ in range(N):
    power *= A
    result += sign * power
    sign *= -1

print(f"Результат: {result}")