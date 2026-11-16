def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


a, b = map(int, input("Введите два целых числа: ").split())
print(gcd(a, b))
