import math

ax, ay = map(float, input("Введите координаты точки A (x y): ").split())
bx, by = map(float, input("Введите координаты точки B (x y): ").split())
cx, cy = map(float, input("Введите координаты точки C (x y): ").split())

distance_b = math.hypot(bx - ax, by - ay)
distance_c = math.hypot(cx - ax, cy - ay)

if distance_b <= distance_c:
	print(f"Точка B ({bx}, {by}) ближе к A; расстояние: {distance_b}")
else:
	print(f"Точка C ({cx}, {cy}) ближе к A; расстояние: {distance_c}")
