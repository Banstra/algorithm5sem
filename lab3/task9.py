import sys


p = float(sys.stdin.readline("Введите процентную ставку: "))
amount = 1000.0
months = 0

while amount <= 1100:
	amount *= 1 + p / 100
	months += 1

print(f"Количество месяцев: {months}")
print(f"Сумма: {amount}")
