def fibonacci(n):
	if n < 0:
		raise ValueError("n должно быть неотрицательным числом")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

a = int(input("Введите число: "))
print(f"Число Фибоначчи для {a} равно {fibonacci(a)}")