# Дано вещественное число A и целое число N (> 0). Найти сумму 1 + A + A^2 + ... + A^N.
a = float(input("Введите вещественное число A: "))
n = int(input("Введите целое число N (> 0): "))

if n <= 0:
	raise ValueError("N должно быть положительным")

summa = 1.0
power = 1.0
for _ in range(n):
	power *= a
	summa += power

print(f"Сумма: {summa}")
