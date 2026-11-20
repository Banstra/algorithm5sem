# Дано целое число N, а также массив из N действительных чисел. Определить, содержится ли в массиве заданное число. Если содержится, то вернуть его позицию в массиве (позиции нумеруются с 1), иначе вернуть -1.
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
array.sort()
target = int(input("Введите число для поиска: "))
result = binary_search(array, target)

if result != -1:
    print(f"Элемент {target} найден на позиции {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")
