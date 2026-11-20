# Дано число, обозначающее цену за килограмм конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.
price_per_kg = float(input("Введите цену за килограмм: "))

for tenths in range(1, 11):
	weight = tenths / 10
	print(f"{weight} кг: {price_per_kg * weight} руб.")