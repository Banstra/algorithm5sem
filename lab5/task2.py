N = int(input("Введите количество членов прогрессии: "))
A = float(input("Введите первый член прогрессии: "))
D = float(input("Введите знаменатель прогрессии: "))

progression = [A * D ** i for i in range(N)]
print(*progression)
