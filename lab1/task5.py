#Даны два ненулевых числа a и b. Найти: сумму модулей, разность модулей, произведение модулей, частное модулей.
first = float(input("Введите первое ненулевое число: "))
second = float(input("Введите второе ненулевое число: "))

first_abs = abs(first) # Модуль первого числа
second_abs = abs(second) # Модуль второго числа

print("Сумма модулей:", first_abs + second_abs)
print("Разность модулей:", first_abs - second_abs)
print("Произведение модулей:", first_abs * second_abs)
print("Частное модулей:", first_abs / second_abs)

