def power(x, n):
	if n < 0:
		return 1 / power(x, -n)
	if n == 0:
		return 1
	half = power(x, n // 2)
	squared = half * half
	return squared if n % 2 == 0 else squared * x

a = float(input("Введите число: "))
b = int(input("Введите целую степень: "))
print(f"{a} в степени {b} равно {power(a, b)}")