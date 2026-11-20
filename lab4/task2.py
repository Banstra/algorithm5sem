# Дано целое число N. Вычислить N-е число Фибоначчи (F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)).
def fibonacci(n):
	if n < 0:
		raise ValueError("n должно быть неотрицательным числом")
	if n <= 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)

a = int(input("Введите число: "))
print(f"Число Фибоначчи для {a} равно {fibonacci(a)}")