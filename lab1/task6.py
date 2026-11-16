import math

x1, y1, x2, y2 = map(float, input("Введите координаты двух точек (x1 y1 x2 y2): ").split())
distance = math.hypot(x2 - x1, y2 - y1)
print(f"Расстояние между точками: {distance}")
