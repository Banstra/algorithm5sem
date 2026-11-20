# Дано целое число N. Вычислить факториал числа N (N! = 1 * 2 * 3 * ... * N). Факториал числа 0 равен 1.
def factorial(n: int) -> int:

    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

a = int(input("Введите число: "))
print(f"Факториал числа {a} равен {factorial(a)}")