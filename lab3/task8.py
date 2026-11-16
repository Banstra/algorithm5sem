N = int(input("Введите число N: "))

K = 0
total = 0

while total < N:
	K += 1
	total += K

print(f"Наименьшее натуральное число K: {K}")
print(f"Сумма: {total}")
