# Дано целое число N. Определить количество цифр в числе N.
def count_digits(number):
    number = abs(number)
    if number < 10:
        return 1
    return 1 + count_digits(number // 10)

num = int(input("Введите число: "))
digit_count = count_digits(num)
print(f"Количество цифр в числе {num}: {digit_count}")