# Дано целое число N (> 0). Найти произведение чисел 1.1 * 1.2 * ... * (1 + N/10).
n = int(input("Введите N (> 0): "))
if n <= 0:
	raise ValueError("N должно быть положительным")

product = 1.0
for i in range(1, n + 1):
	product *= 1 + i / 10

print(f"Произведение: {product}")
