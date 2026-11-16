def find_duplicate_indices(values):
	first_index = {}
	for index, value in enumerate(values, start=1):
		if value in first_index:
			return first_index[value], index
		first_index[value] = index
	raise ValueError("Различные элементы не найдены")


n = int(input())
values = list(map(int, input("Введите элементы через пробел: ").split()))
if len(values) != n:
	raise ValueError("Количество элементов не соответствует введенному числу")
print(*find_duplicate_indices(values))

