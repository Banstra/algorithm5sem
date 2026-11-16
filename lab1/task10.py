import math


coordinates = list(map(float, input("Введите координаты трех точек (x1 y1 x2 y2 x3 y3): ").split()))
x1, y1, x2, y2, x3, y3 = coordinates

side1 = math.hypot(x2 - x1, y2 - y1)
side2 = math.hypot(x3 - x2, y3 - y2)
side3 = math.hypot(x1 - x3, y1 - y3)

perimeter = side1 + side2 + side3
area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

print("Периметр:", perimeter)
print("Площадь:", area)
