# Дано два целых числа a и b. Вывести все числа от a до b включительно.
a, b = map(int, input("Введите два целых числа a и b: ").split())

for number in range(a, b + 1):
	print(number)	
