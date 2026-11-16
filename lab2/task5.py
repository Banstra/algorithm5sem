number = int(input("Введите целое число: "))

if number == 0:
	print("нулевое число")
else:
	sign = "положительное" if number > 0 else "отрицательное"
	parity = "четное" if number % 2 == 0 else "нечетное"
	print(f"{sign} {parity} число")
