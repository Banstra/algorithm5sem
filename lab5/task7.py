## Дано целое число N, а также массив из N действительных чисел. Определить разность между соседними элементами массива. Если разность между всеми соседними элементами одинакова, то вернуть эту разность, иначе вернуть 0.
def common_difference(values):
	if len(values) < 2:
		return 0

	ordered = sorted(values)
	difference = ordered[1] - ordered[0]
	if all(ordered[i] - ordered[i - 1] == difference for i in range(2, len(ordered))):
		return difference
	return 0


n = int(input("Введите количество элементов массива: "))
numbers = list(map(int, input("Введите элементы через пробел: ").split()))
print(common_difference(numbers[:n]))
