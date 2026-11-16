n = int(input("Введите количество элементов массива: "))
values = list(map(int, input("Введите элементы через пробел: ").split()))[:n]

left, right = 0, len(values) - 1
result = []
while left <= right:
	result.append(values[left])
	left += 1
	if left <= right:
		result.append(values[right])
		right -= 1

print(*result)
