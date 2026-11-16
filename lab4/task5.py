def binary_search(array, target, left=0, right=None):
	if right is None:
		right = len(array) - 1

	if left > right:
		return -1

	middle = (left + right) // 2
	if array[middle] == target:
		return middle
	if array[middle] < target:
		return binary_search(array, target, middle + 1, right)
	return binary_search(array, target, left, middle - 1)

array = list(map(int, input("Введите элементы массива через пробел: ").split()))
target = int(input("Введите число для поиска: "))
result = binary_search(array, target)

if result != -1:
    print(f"Элемент {target} найден на позиции {result + 1}.")
else:
    print(f"Элемент {target} не найден в массиве.")
