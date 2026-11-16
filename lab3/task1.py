price_per_kg = float(input("Введите цену за килограмм: "))

for tenths in range(1, 11):
	weight = tenths / 10
	print(f"{weight} кг: {price_per_kg * weight} руб.")