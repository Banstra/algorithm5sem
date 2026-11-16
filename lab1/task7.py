a, b, c = map(float, input("Введите координаты трех точек (a b c): ").split())

ac = abs(c - a)
bc = abs(c - b)

print(f"Расстояние от точки A до точки C: {ac}")
print(f"Расстояние от точки B до точки C: {bc}")
print(f"Сумма расстояний: {ac + bc}")
