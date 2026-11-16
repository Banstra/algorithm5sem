number = int(input("Введите число от 1 до 999: "))

if number < 1 or number > 999:
	raise ValueError("Число должно быть в диапазоне от 1 до 999")

parity = "четное" if number % 2 == 0 else "нечетное"
digits = "однозначное" if number < 10 else "двузначное" if number < 100 else "трехзначное"

print(f"{parity} {digits} число")
