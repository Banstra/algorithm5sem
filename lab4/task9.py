def hanoi(n, source, auxiliary, target):

    if n == 1:
        print(f"Переложить диск 1 с {source} на {target}")
        return

    hanoi(n - 1, source, target, auxiliary)
    print(f"Переложить диск {n} с {source} на {target}")
    hanoi(n - 1, auxiliary, source, target)


# Пример использования
n = int(input("Введите количество дисков: "))
hanoi(n, 'A', 'B', 'C')
