a, b = map(int, input("Введите два целых числа a и b: ").split())

for number in range(a, b + 1):
	for _ in range(number):
		print(number)
