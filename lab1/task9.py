x1, y1, x2, y2 = map(float, input("Введите координаты двух точек (x1 y1 x2 y2): ").split())

width = abs(x2 - x1)
height = abs(y2 - y1)

print(f"Периметр прямоугольника: {2 * (width + height)}")
print(f"Площадь прямоугольника: {width * height}")