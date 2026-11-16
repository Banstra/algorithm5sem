
def reorder(values):
	return values[::2] + values[1::2][::-1]


def main():
	n = int(input("Введите количество элементов массива: "))
	values = list(map(int, input("Введите элементы через пробел: ").split()))
	print(*reorder(values[:n]))


if __name__ == "__main__":
	main()
