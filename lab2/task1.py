
A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A == B:
	A = B = 0
else:
	A = B = max(A, B)

print(f"A = {A}, B = {B}")
